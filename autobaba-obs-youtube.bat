@echo off

if [%1]==[] goto default

ffmpeg -i %1 -c:v libx264 -preset slow -crf 18 -vf "scale=2560:1440:flags=neighbor:force_original_aspect_ratio=decrease,pad=2560:1440:(ow-iw)/2:(oh-ih)/2,setsar=1" autobaba-obs-youtube.mkv

pause

goto :eof

:default

ffmpeg -i autobaba-obs-lossless.avi -c:v libx264 -preset slow -crf 18 -vf "scale=2560:1440:flags=neighbor:force_original_aspect_ratio=decrease,pad=2560:1440:(ow-iw)/2:(oh-ih)/2,setsar=1" autobaba-obs-youtube.mkv

pause