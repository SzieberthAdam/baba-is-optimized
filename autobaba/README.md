Autobaba
========

Autobaba is a toolbar to note, test, and publish solutions.


Dependencies
------------

First, install the following softwares:

* AutoHotkey
* Python 3

If you want to record solution videos then you also need the following softwares to get installed on your PC:

* FFmpeg
* OBS Studio


Usage
-----

1. Start *Baba Is You* in windowed mode (fullscreen off).
2. Run `autobaba-work.bat`. It will update your `autobaba.ahk` file automatically every time you save `autobaba.txt`.
3. Open `autobaba.txt` with *Notepad*
4. Start solving a level using the correct [format](https://github.com/SzieberthAdam/baba-is-you-solutions#solution-format). Note down only some several actions at a time then continue with the next point.
5. Save `autobaba.txt`.
6. For the first time, run `autobaba.ahk`. An *AutoHotkey* icon should appear in your system tray: ![AutoHotkey Tray Icon](https://raw.githubusercontent.com/SzieberthAdam/baba-is-you-solutions/master/autobaba/img/AHK-Icon5.png). If *AutoHotkey* is already running, reload the script by pressing `Ctrl+R` which also restarts the level.
7. Run your macro by pressing `Ctrl+B`. You should see your solution replayed live on screen.
8. If the level is not yet won then go back to point 3.
9. Once finished, run `autobaba.bat` which creates your final `autobaba.ahk`.
10. Copy and rename `autobaba.txt` and `autobaba.ahk` files to a safe place. I recommend using my name format: `Level Cavern-11, Trick Door, 114.txt` and `Level Cavern-11, Trick Door, 114.ahk`. Here the solution was done in 114 time units. To get the number of time units of `autobaba.txt`, run the `linecount.bat` batch file. However, I prefer using a text editor which shows line count in the first place like [Notepad2](https://www.flos-freeware.ch/notepad2.html) which is a portable lightweight one.
11. Finally, run `reset.bat` to clean up `autobaba.txt` and `autobaba.ahk` files.


Video Recording
---------------

First, set up *Baba Is You* and *OBS Studio* according to the [instructions in the OBS subdirectory](https://github.com/SzieberthAdam/baba-is-you-solutions/tree/master/autobaba/OBS).

1. Follow [Usage](#usage) from point 1 to point 9. Make sure that *Baba Is You* window was not resized and has its original size (game canvas: 854x480).
2. Once finished, run `autobaba-obs.bat` which creates your final `autobaba.ahk`. This AutoHotkey file is optimized for OBS recording.
3. Run or refresh the `autobaba.ahk` script.
4. Start OBS Studio. You should see the *Baba In You* window in the top left section of the OBS canvas.
5. In *Baba In You*, in the map, navigate to the location where `Enter` key would start the level.
6. Start the recording by pressing `Ctrl+B` in the game. It should control both *OBS Studio* and *Baba Is You* in the same time. Start and stop of the recording should also be automated.
7. Once done, there should be a new `.AVI` file in your Windows user's `Video` directory. Rename it to `autobaba-obs.avi` and copy it to this very directory.
8. Run `autobaba-obs-lossless.bat`. It should produce a 10–20 MB size file named `autobaba-obs-lossless.avi`. This is your reference video file which I recommend to keep.
9. Watch this recording to make sure it contains everything it has to. If you use VLC, set it up to use the Windows GDI video output for nearest neighbour scaling and sharpness.
10. If you want to publish your recording on *YouTube*, then run `autobaba-obs-youtube.bat`. It will create a 2560x1440 size video for *YouTube*. This conversion is required as *YouTube* would blur the uploaded lossless video.
11. Follow [Usage](#usage) from point 10 to point 12.
