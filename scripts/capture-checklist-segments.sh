#!/bin/bash
# Capture the authenticated client-side footage (segments s03..s06) for the
# capabilities video, WITHOUT screen-recording.
#
# Usage:  ./capture-checklist-segments.sh '<magic-link-verify-URL>'
#
# Why it takes a magic link: metis/10 is behind a session, and headless Chrome
# starts with an empty cookie jar. Visiting the verify URL once with a
# persistent --user-data-dir puts the session cookie in that profile; every
# capture after it is signed in. Get the link by requesting a sign-in email at
# metiscortex.au and copying the URL out of the email (it is single-use and
# expires, so run this soon after).
#
# This replaces screen recording deliberately. screencapture -v grabs the whole
# display, so it captures whatever window is frontmost — which on three
# attempts was a different Chrome window, not the automated tab. Headless
# full-page stills + ffmpeg pans are deterministic and can only ever contain
# the page requested.

set -euo pipefail
LINK="${1:?usage: capture-checklist-segments.sh '<magic-link-verify-URL>'}"

# Fail fast on the obvious mistake: running this with the placeholder still in
# place. Chrome will happily "succeed" on a non-URL and screenshot a blank page.
case "$LINK" in
  http://*|https://*) ;;
  *) echo "!! That is not a URL: '$LINK'"
     echo "   Request a sign-in email at metiscortex.au and paste the link from"
     echo "   it, in single quotes. It is single-use and expires."
     exit 1 ;;
esac
CHROME="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
CAP="$HOME/Desktop/metis-demo/capabilities"
PROFILE="$CAP/.authprofile"
STILLS="$CAP/stills"
SEG="$CAP/segments"
BASE="${METIS_BASE:-https://metis-cortex.fly.dev}"
MATTER="${METIS_MATTER:-10}"
mkdir -p "$STILLS" "$SEG"

# headless Chrome never exits on its own here, so: run it, wait for the file,
# then kill it.
grab () { # outfile, url, height
  rm -f "$1"
  ( "$CHROME" --headless --disable-gpu --no-sandbox --hide-scrollbars \
      --user-data-dir="$PROFILE" --window-size=1600,"$3" \
      --screenshot="$1" "$2" >/dev/null 2>&1 ) &
  local pid=$!
  for _ in $(seq 1 40); do [ -s "$1" ] && break; sleep 1; done
  sleep 2; kill $pid 2>/dev/null || true; wait $pid 2>/dev/null || true
  [ -s "$1" ] || { echo "!! failed to capture $2"; exit 1; }
}

echo "1/3  signing the headless profile in…"
grab "$STILLS/.auth.png" "$LINK" 1000
rm -f "$STILLS/.auth.png"

echo "2/3  capturing matter pages…"
grab "$STILLS/checklist-tall.png" "$BASE/metis/$MATTER"               6000
grab "$STILLS/chat-tall.png"      "$BASE/metis/$MATTER?tab=chat"      2200
grab "$STILLS/docs-tall.png"      "$BASE/metis/$MATTER?tab=documents" 2200

# Verify we actually captured a PAGE, not a blank canvas.
#
# Do NOT check image height here: headless Chrome always returns exactly the
# --window-size height regardless of what rendered, so a height check passes on
# a completely blank page. (It did exactly that on 2026-08-06 and reported
# success over 48s of empty cream.) Measure the pixels instead — luma standard
# deviation is ~0 on a flat background and >15 on a page with text on it.
# (ffmpeg's signalstats filter is not in every build — measured directly
# instead, which needs nothing beyond ffmpeg + python3. Reference values:
# a real page reads 68–105, a blank one reads 0.0.)
ystd () {
  ffmpeg -v error -i "$1" -vf "scale=200:-1,format=gray" -f rawvideo - 2>/dev/null \
  | python3 -c "
import sys,statistics
d=sys.stdin.buffer.read()
print(f'{statistics.pstdev(d):.1f}' if d else '0.0')"
}
for still in checklist-tall chat-tall docs-tall; do
  sd=$(ystd "$STILLS/$still.png")
  echo "     $still  pixel-spread=${sd:-?}"
  if [ -z "$sd" ] || [ "$(printf '%.0f' "$sd")" -lt 8 ]; then
    echo
    echo "!! $still.png is essentially blank — nothing rendered."
    echo "   Almost always means the sign-in did not take: the magic link was"
    echo "   already used, expired, or was not a real link. Request a fresh"
    echo "   sign-in email and run this again with the new link."
    echo "   Removing the stills so nothing downstream uses them."
    rm -f "$STILLS/checklist-tall.png" "$STILLS/chat-tall.png" "$STILLS/docs-tall.png"
    rm -f "$SEG"/s03.mp4 "$SEG"/s04.mp4 "$SEG"/s05.mp4 "$SEG"/s06.mp4
    exit 1
  fi
done

echo "3/3  rendering pans…"
H=$(ffprobe -v error -show_entries stream=height -of csv=p=0 "$STILLS/checklist-tall.png")
pan () { # name, still, dur, y0, y1
  ffmpeg -y -loop 1 -i "$2" -t "$3" -r 30 \
    -vf "crop=1600:850:0:'$4+($5-$4)*(t/$3)',format=yuv420p" \
    -c:v libx264 -preset medium -crf 20 "$SEG/$1.mp4" -loglevel error
  printf "  %-4s %ss\n" "$1" \
    "$(ffprobe -v error -show_entries format=duration -of csv=p=0 "$SEG/$1.mp4")"
}

# Durations are pinned to the narration lines they sit under — do not change
# them without re-checking voices/n03..n06.wav.
pan s03 "$STILLS/checklist-tall.png" 14.07 0                      $((H*30/100))
pan s04 "$STILLS/checklist-tall.png"  9.75 $((H*30/100))          $((H*52/100))
pan s05 "$STILLS/checklist-tall.png" 12.59 $((H*62/100))          $((H-850))
pan s06 "$STILLS/chat-tall.png"      12.03 0                      600

echo
echo "done. Now run:"
echo "  ~/dev/metis/scripts/render-capabilities-video.sh"
echo
echo "Eyeball $STILLS/checklist-tall.png first — if the lawyer-flag item or the"
echo "process gates fall outside the pan ranges above, nudge the percentages."
