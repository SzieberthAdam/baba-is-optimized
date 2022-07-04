ffmpeg -i autobaba-obs.avi -c:v utvideo -c:a copy -filter:v "crop=854:480:0:0" autobaba-obs-lossless.avi
