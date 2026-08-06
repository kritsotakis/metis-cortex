#!/bin/bash
# Assemble the Metis Cortex capabilities video.
#
# Usage:  ./render-capabilities-video.sh [out.mp4]
#
# Inputs live in ~/Desktop/metis-demo/capabilities/
#   voices/n00..n15.wav   — narration, already loudnorm'd to EBU R128 (I=-16)
#   segments/s00,s01,s02,s14,s15.mp4  — 1600x850 pans over headless full-page stills
#   segments/s03..s06.mp4 — checklist footage. NOT YET CAPTURED (see below).
# plus ~/Desktop/metis-demo/metis-demo.mp4 (1600x850, 108.125s) for the solicitor half.
#
# WHY THE CHECKLIST SEGMENTS ARE MISSING
# --------------------------------------
# s03..s06 show an authenticated matter (metis/10): the 17-item checklist, the
# lawyer-flag on the s60I item, the process gates, and the Ask Metis/Documents
# tabs. They can't be produced headlessly because those pages need a session,
# and three screen-recording attempts captured the wrong Chrome window
# (screencapture -v records the whole display; the automated tab was not the
# frontmost window). Capture them with capture-checklist-segments.sh, which
# fronts the right window and verifies before recording.
#
# NOTE: amix must use duration=longest. duration=first truncates the whole mix
# to the first delayed input and silently kills the rest of the track.

set -euo pipefail
CAP="$HOME/Desktop/metis-demo/capabilities"
V="$CAP/voices"
SEG="$CAP/segments"
SOLICITOR="$HOME/Desktop/metis-demo/metis-demo.mp4"
OUT="${1:-$HOME/Desktop/metis-demo/metis-capabilities.mp4}"
WORK="$(mktemp -d)"
trap 'rm -rf "$WORK"' EXIT

have_checklist=1
for s in s03 s04 s05 s06; do [ -f "$SEG/$s.mp4" ] || have_checklist=0; done
if [ "$have_checklist" -eq 0 ]; then
  echo "!! segments s03..s06 missing — run capture-checklist-segments.sh first."
  echo "   Building a PARTIAL video: the client half will jump from the guides"
  echo "   index straight to the solicitor side, and narration n03..n06 is omitted."
  echo
fi

dur () { ffprobe -v error -show_entries format=duration -of csv=p=0 "$1"; }

# ---- video: concat the segments in order -------------------------------------
CLIENT_SEGS=(s00 s01 s02)
[ "$have_checklist" -eq 1 ] && CLIENT_SEGS+=(s03 s04 s05 s06)

: > "$WORK/list.txt"
for s in "${CLIENT_SEGS[@]}"; do echo "file '$SEG/$s.mp4'" >> "$WORK/list.txt"; done
echo "file '$SOLICITOR'" >> "$WORK/list.txt"
for s in s14 s15; do echo "file '$SEG/$s.mp4'" >> "$WORK/list.txt"; done

ffmpeg -y -f concat -safe 0 -i "$WORK/list.txt" \
  -c:v libx264 -preset medium -crf 20 -r 30 -pix_fmt yuv420p -an \
  "$WORK/video.mp4" -loglevel error

# ---- audio: lay each narration line at the start of its own segment ----------
# Client + close lines are 1:1 with their segment and equal length, so each one
# starts 0.25s into its segment. The solicitor block is a single 108s take, so
# its lines (n07..n13) are pinned to what is actually on screen in it:
#   0:00 dashboard · 0:10 case brief · 0:35 issues · 1:00 research
#   1:15 compliance · 1:35 client portal
# n08 introduces the conference, so the consultation excerpt plays straight
# after it, before n09 starts talking over the brief.
SOLICITOR_CUES=(0.4 7.5 30.0 54.5 65.0 71.5 93.4)   # n07 n08 n09 n10 n11 n12 n13
SOLICITOR_LINES=(n07 n08 n09 n10 n11 n12 n13)
CONV_CUE=12.5      # excerpt of the client conference, under the dashboard/brief
CONV_LEN=16

# i starts at 1: input 0 of the final ffmpeg call is the silent video.
inputs=(); filters=(); labels=(); i=1; t=0

add () { # wavname, absolute_start
  inputs+=(-i "$V/$1.wav")
  local ms; ms=$(printf '%.0f' "$(echo "$2 * 1000" | bc -l)")
  filters+=("[$i:a]adelay=${ms}|${ms}[a$i];")
  labels+=("[a$i]"); i=$((i+1))
}

for s in "${CLIENT_SEGS[@]}"; do
  add "n${s#s}" "$(echo "$t + 0.25" | bc -l)"
  t=$(echo "$t + $(dur "$SEG/$s.mp4")" | bc -l)
done

for k in "${!SOLICITOR_LINES[@]}"; do
  add "${SOLICITOR_LINES[$k]}" "$(echo "$t + ${SOLICITOR_CUES[$k]}" | bc -l)"
done

# The conference excerpt: two voices, matched to the same loudness as narration
# so it doesn't jump, with a short fade out of the cut.
ffmpeg -y -ss 0 -t "$CONV_LEN" -i "$HOME/Desktop/metis-demo/consultation-demo.mp3" \
  -af "loudnorm=I=-16:TP=-1.5:LRA=11,afade=t=out:st=$((CONV_LEN-2)):d=2" \
  -ar 44100 -ac 2 "$WORK/conv.wav" -loglevel error
inputs+=(-i "$WORK/conv.wav")
CONV_MS=$(printf '%.0f' "$(echo "($t + $CONV_CUE) * 1000" | bc -l)")
filters+=("[$i:a]adelay=${CONV_MS}|${CONV_MS}[a$i];")
labels+=("[a$i]"); i=$((i+1))

t=$(echo "$t + $(dur "$SOLICITOR")" | bc -l)

for s in s14 s15; do
  add "n${s#s}" "$(echo "$t + 0.25" | bc -l)"
  t=$(echo "$t + $(dur "$SEG/$s.mp4")" | bc -l)
done

ffmpeg -y -i "$WORK/video.mp4" "${inputs[@]}" \
  -filter_complex "$(IFS=; echo "${filters[*]}")$(IFS=; echo "${labels[*]}")amix=inputs=$((i-1)):normalize=0:duration=longest[m];[m]alimiter=limit=0.95,apad[aout]" \
  -map 0:v -map "[aout]" -c:v copy -c:a aac -b:a 160k -shortest \
  "$OUT" -loglevel error

echo "wrote $OUT  ($(dur "$OUT")s)"
for probe in 5 20 45 80 130 175; do
  printf "  %4ss: %s dB\n" "$probe" \
    "$(ffmpeg -ss $probe -t 3 -i "$OUT" -af volumedetect -f null - 2>&1 \
       | grep mean_volume | grep -o '\-[0-9.]*' || echo n/a)"
done
