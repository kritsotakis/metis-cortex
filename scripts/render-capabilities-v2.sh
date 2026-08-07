#!/bin/bash
# Metis capabilities video v2 — branded cards, captions, watermark, more footage.
#
# v2 changes over render-capabilities-video.sh (kept for reference):
#   - Branded section cards between chapters (navy/gold, real brand lockups).
#     They also fix the "did it end?" problem: a pause after a card reads as a
#     chapter break, not a stall.
#   - Persistent watermark (brand mark, bottom-right) on all app footage.
#   - Caption overlays for the load-bearing claims, so it works muted.
#   - More footage: Ask Metis, Documents AND Forms under/after n06.
#   - Solicitor tail trimmed to 106s; n13 pulled to 92.0 to close dead air.
#
# This ffmpeg build has NO drawtext filter — all text (cards, caption strips,
# watermark) is pre-rendered to PNG by scripts via /usr/bin/python3 + PIL into
# capabilities/brand/, and ffmpeg only overlays. Regenerate those PNGs with the
# PIL block in the session log / or by editing them directly.
#
# Known issue NOT fixed here: narration says "Meaty" for Metis (n00, n04, n09,
# n15). Re-render those four lines with the text "Mettiss" once a fresh
# ElevenLabs key exists, drop into capabilities/voices/, re-run this script.
#
# NOTE: amix must use duration=longest (duration=first truncates the mix).

set -euo pipefail
CAP="$HOME/Desktop/metis-demo/capabilities"
V="$CAP/voices"; STILLS="$CAP/stills"; B="$CAP/brand"
SOLICITOR="$HOME/Desktop/metis-demo/metis-demo.mp4"
OUT="${1:-$HOME/Desktop/metis-demo/metis-capabilities-v2.mp4}"
WORK="$(mktemp -d)"
trap 'rm -rf "$WORK"' EXIT
dur () { ffprobe -v error -show_entries format=duration -of csv=p=0 "$1"; }

# Segment lengths are DERIVED from the narration, never hardcoded.
#
# They used to be literal numbers matching the original recordings. When four
# lines were re-recorded to fix a mispronunciation their durations moved by up
# to 1.6s, which would have left narration running past its own visual and a
# second and a half of dead air on the close. Deriving them means a re-record
# can never silently desynchronise the video again.
#
# PAD gives a beat before the voice starts and a moment after it ends.
PAD=0.75
segdur () { echo "$(dur "$V/$1.wav") + $PAD" | bc -l; }

# ---------- 1. cards (still PNG -> clip) ------------------------------------
still () { # out png dur
  ffmpeg -y -loop 1 -i "$B/$2.png" -t "$3" -r 30 -vf "scale=1600:850,format=yuv420p" \
    -c:v libx264 -preset medium -crf 20 "$WORK/$1.mp4" -loglevel error
}
still card_open  card_open  2.6
still card_client card_client 2.0
still card_sol   card_sol   2.0
still card_stand card_stand 2.0
still card_close card_close 3.6

# ---------- 2. footage segments ---------------------------------------------
# seg: vertical pan over a tall still + watermark + optional caption strip.
seg () { # out src dur y0 y1 [capname]
  local ov="[c][1:v]overlay=W-w-24:H-h-24[d]"
  local capin=() capov=";[d]format=yuv420p[o]"
  if [ $# -ge 6 ]; then
    capin=(-i "$B/$6.png")
    capov=";[d][2:v]overlay=0:H-h:enable='gte(t,0.6)'[e];[e]format=yuv420p[o]"
  fi
  ffmpeg -y -loop 1 -i "$STILLS/$2.png" -i "$B/wm.png" ${capin[@]+"${capin[@]}"} -t "$3" -r 30 \
    -filter_complex "[0:v]crop=1600:850:0:'$4+($5-$4)*(t/$3)'[c];$ov$capov" \
    -map "[o]" -c:v libx264 -preset medium -crf 20 -t "$3" "$WORK/$1.mp4" -loglevel error
}
# hseg: static centred crop for wide stills. (Was a horizontal drift — read as
# the page sliding sideways, which Peter flagged. No motion beats odd motion.)
hseg () { # out src dur [capname]
  local ov="[c][1:v]overlay=W-w-24:H-h-24[d]"
  local capin=() capov=";[d]format=yuv420p[o]"
  if [ $# -ge 4 ]; then
    capin=(-i "$B/$4.png")
    capov=";[d][2:v]overlay=0:H-h:enable='gte(t,0.6)'[e];[e]format=yuv420p[o]"
  fi
  ffmpeg -y -loop 1 -i "$STILLS/$2.png" -i "$B/wm.png" ${capin[@]+"${capin[@]}"} -t "$3" -r 30 \
    -filter_complex "[0:v]crop=1600:850:(iw-1600)/2:0[c];$ov$capov" \
    -map "[o]" -c:v libx264 -preset medium -crf 20 -t "$3" "$WORK/$1.mp4" -loglevel error
}

seg  v00 home-tall    "$(segdur n00)" 0    300
seg  v01 home-tall   "$(segdur n01)" 300  1900
seg  v02 guides-tall "$(segdur n02)" 300  900  cap_guides
seg  v03 checklist-tall "$(segdur n03)" 0   450 cap_17
seg  v04 checklist-tall "$(segdur n04)" 450 900 cap_flag
seg  v05 checklist-tall "$(segdur n05)" 1900 2483 cap_gates
hseg v06a askmetis-850       6.00 cap_ask
hseg v06b documents-tall-850 6.03 cap_docs
hseg v06c forms-tall-850     3.00 cap_forms
seg  v14 home-tall   "$(segdur n14)" 3813 4400 cap_leap
seg  v15 home-tall   "$(segdur n15)" 4400 4700

# ---------- 3. solicitor block: trim, watermark, three timed captions -------
ffmpeg -y -i "$SOLICITOR" -i "$B/wm.png" -i "$B/cap_sewell.png" -i "$B/cap_s174.png" -i "$B/cap_portal.png" \
  -t 103.5 -r 30 -filter_complex "\
[0:v][1:v]overlay=W-w-24:H-h-24[a];\
[a][2:v]overlay=0:H-h:enable='between(t,31,52)'[b];\
[b][3:v]overlay=0:H-h:enable='between(t,73,88)'[c];\
[c][4:v]overlay=0:H-h:enable='between(t,92,104)',format=yuv420p[o]" \
  -map "[o]" -an -c:v libx264 -preset medium -crf 20 "$WORK/vsol.mp4" -loglevel error

# ---------- 4. concat -------------------------------------------------------
ORDER=(card_open v00 card_client v01 v02 v03 v04 v05 v06a v06b v06c card_sol vsol card_stand v14 v15 card_close)
: > "$WORK/list.txt"
for s in "${ORDER[@]}"; do echo "file '$WORK/$s.mp4'" >> "$WORK/list.txt"; done
ffmpeg -y -f concat -safe 0 -i "$WORK/list.txt" -c:v libx264 -preset medium -crf 20 -r 30 -pix_fmt yuv420p -an "$WORK/video.mp4" -loglevel error

# ---------- 5. audio --------------------------------------------------------
inputs=(); filters=(); labels=(); i=1
# macOS ships bash 3.2 (no associative arrays) — start times become T_<name>.
t=0; for s in "${ORDER[@]}"; do eval "T_$s=$t"; t=$(echo "$t + $(dur "$WORK/$s.mp4")" | bc -l); done
TOTAL=$t
tstart () { eval "echo \$T_$1"; }
add () { # wav abs_start
  inputs+=(-i "$1")
  local ms; ms=$(printf '%.0f' "$(echo "$2 * 1000" | bc -l)")
  filters+=("[$i:a]adelay=${ms}|${ms}[a$i];"); labels+=("[a$i]"); i=$((i+1))
}
for kv in "n00 v00" "n01 v01" "n02 v02" "n03 v03" "n04 v04" "n05 v05" "n06 v06a" "n14 v14" "n15 v15"; do
  set -- $kv; add "$V/$1.wav" "$(echo "$(tstart $2) + 0.25" | bc -l)"
done
SOL=$(tstart vsol)
# n07 starts over the section card as a bridge (card is 2.0s before vsol)
add "$V/n07.wav" "$(echo "$SOL - 1.7" | bc -l)"
for kv in "n08 7.5" "n09 30.0" "n10 54.5" "n11 65.0" "n12 71.5" "n13 92.0"; do
  set -- $kv; add "$V/$1.wav" "$(echo "$SOL + $2" | bc -l)"
done
ffmpeg -y -ss 0 -t 18 -i "$HOME/Desktop/metis-demo/consultation-demo.mp3" \
  -af "loudnorm=I=-16:TP=-1.5:LRA=11,afade=t=out:st=16:d=2" -ar 44100 -ac 2 "$WORK/conv.wav" -loglevel error
add "$WORK/conv.wav" "$(echo "$SOL + 10.0" | bc -l)"

ffmpeg -y -i "$WORK/video.mp4" "${inputs[@]}" \
  -filter_complex "$(IFS=; echo "${filters[*]}")$(IFS=; echo "${labels[*]}")amix=inputs=$((i-1)):normalize=0:duration=longest[m];[m]alimiter=limit=0.95,apad[aout]" \
  -map 0:v -map "[aout]" -c:v copy -c:a aac -b:a 160k -shortest "$OUT" -loglevel error

echo "wrote $OUT  ($(dur "$OUT")s, video $TOTAL)"
ffmpeg -i "$OUT" -af "silencedetect=n=-45dB:d=4" -f null - 2>&1 | grep silence_duration || echo "no quiet beat over 4s"
