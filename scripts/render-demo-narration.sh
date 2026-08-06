#!/bin/bash
# Re-render the Metis demo video's audio track.
#
# Usage:  ./render-demo-narration.sh <voices-dir> [out.mp4]
#
# <voices-dir> must contain, at 44.1kHz stereo:
#   conv.wav  — the client-conference excerpt (both speakers), ~16s
#   n00..n07.wav — the eight narration lines, in order
#
# The start times below are pinned to what is on screen in metis-demo.mp4.
# If the video is re-recorded, re-check them before trusting this.
#
# NOTE: amix must use duration=longest. Using duration=first truncates the whole
# mix to the first delayed input (~22s) and silently kills the rest of the track.

set -euo pipefail
VOICES="${1:?usage: render-demo-narration.sh <voices-dir> [out.mp4]}"
OUT="${2:-$HOME/Desktop/metis-demo/metis-demo-narrated.mp4}"
VIDEO="$HOME/Desktop/metis-demo/metis-demo.mp4"
DUR=108.125

ffmpeg -y \
  -i "$VIDEO" \
  -i "$VOICES/conv.wav" \
  -i "$VOICES/n00.wav" -i "$VOICES/n01.wav" -i "$VOICES/n02.wav" -i "$VOICES/n03.wav" \
  -i "$VOICES/n04.wav" -i "$VOICES/n05.wav" -i "$VOICES/n06.wav" -i "$VOICES/n07.wav" \
  -filter_complex "\
   [1:a]adelay=6000|6000[a1];\
   [2:a]adelay=500|500[a2];\
   [3:a]adelay=23000|23000[a3];\
   [4:a]adelay=28000|28000[a4];\
   [5:a]adelay=48500|48500[a5];\
   [6:a]adelay=59500|59500[a6];\
   [7:a]adelay=72000|72000[a7];\
   [8:a]adelay=81500|81500[a8];\
   [9:a]adelay=95000|95000[a9];\
   [a1][a2][a3][a4][a5][a6][a7][a8][a9]amix=inputs=9:normalize=0:duration=longest[m];\
   [m]alimiter=limit=0.95,apad[aout]" \
  -map 0:v -map "[aout]" -c:v copy -c:a aac -b:a 160k -t "$DUR" \
  "$OUT" -loglevel error

echo "wrote $OUT"
for t in 10 30 55 75 90 100; do
  printf "  %3ss: %s dB\n" "$t" \
    "$(ffmpeg -ss $t -t 3 -i "$OUT" -af volumedetect -f null - 2>&1 | grep mean_volume | grep -o '\-[0-9.]*')"
done
