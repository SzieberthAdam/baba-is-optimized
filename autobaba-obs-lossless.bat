@echo off

if [%1]==[] goto default

ffmpeg -i %1 -c:v libx264 -profile:v high444 -crf 0 -c:a copy -filter:v "crop=854:480:0:0" autobaba-obs-lossless.avi

pause

goto :eof

:default

ffmpeg -i autobaba-obs.avi -c:v libx264 -profile:v high444 -crf 0 -c:a copy -filter:v "crop=854:480:0:0" autobaba-obs-lossless.avi

pause