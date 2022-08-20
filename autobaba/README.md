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

1. Start *Baba Is You* in windowed mode (fullscreen off). Make sure that *Baba Is You* window was not resized and has its original size (game canvas: 854x480).
2. Run `autobaba-obs.bat` which updates `autobaba.ahk`. This AutoHotkey file is optimized for OBS recording.
3. Start AutoHotkey with the `autobaba.ahk` script. If AutoHotkey is already running, you have to manually refresh the script by right clicking on its icon in the tray.
4. Start OBS Studio. You should see the *Baba In You* window in the top left section of the OBS canvas.
5. In *Baba In You*, in the map, navigate to the location where `Enter` key would start the level.
6. Start the recording by pressing `Ctrl+B` in the game. It should control both *OBS Studio* and *Baba Is You* in the same time. Start and stop of the recording should also be automated.
7. Once done, there should be a new `.AVI` file in your Windows user's `Video` directory. Rename it to `autobaba-obs.avi` and copy it to this very directory.
8. Run `autobaba-obs-lossless.bat`. It should produce a 10–20 MB size file named `autobaba-obs-lossless.avi`. This is your reference video file which I recommend to keep.
9. Watch this recording to make sure it contains everything it has to. If you use VLC, set it up to use the Windows GDI video output for nearest neighbour scaling and sharpness.
10. If you want to publish your recording on *YouTube*, then run `autobaba-obs-youtube.bat`. It will create a 2560x1440 size video for *YouTube*. This conversion is required as *YouTube* would blur the uploaded lossless video.
11. Follow [Usage](#usage) from point 10 to point 12.


Multiline Solution Format
-------------------------

Autobaba usese the following solution format:

The syntax of a solution is very simple.
Solutions are stored in plain text files with `.TXT` extension.

```
L
L
D
L # -WALL IS STOP
U
U
U
U
U
U
U
U
R
R
D
R
R
U
L
L
L # +WALL IS WIN
D
D
D
wD
```

This is the shortest solution of *Level 1: Where Do I Go?*, done in 25 time units.
[See it in this repo](https://github.com/SzieberthAdam/baba-is-you-solutions/blob/master/BABA%20IS%20YOU/solutions/Level-1%2C%20Where%20Do%20I%20Go(q)%2C%2025.txt).
[Watch the solution by Alayric](https://youtu.be/42OOvZxvH6k).
You can count the lines one-by-one to get the time units the solution takes which is 25.
I rather recommend using a text editor which has line numbering to see how many.
I personally use [Notepad2](https://www.flos-freeware.ch/notepad2.html).

### Actions

Only actions are required for a valid solution file. One action per line, one line per action! No empty lines!

* `U`: up
* `D`: down
* `L`: left
* `R`: right
* `.`: wait (space key)

### Comments and Rule Changes

Solutions may contain comments in any action line and after a `#`.

Rule changes are a special type of comment.
By convention, a rule changes each start with `-` or `+` characters, separated by `;` characters, and are noted with upper case letters.
If you want rule changes and comment noted in the same line, start with rule changes and then put a second `#` to separate your comment properly, finally end with the comment.
*Always note every rule changes or none!*
Rule changes are useful for the solution viewer as it helps the pairing of the text and the video.

### Indicators

Indicators are optional.
They indicate special events which may require some extra wait time in the video solution.
Besides, they provide some extra anchors for the solution viewer with the pairing of the text and the video.

* `?`: indicates a criterion, usually a desired outcome of a random event; put before action and describe the criterion in comment
* `w`: indicates a win condition; put before action
* `y`: indicates that YOU condition has been ended; put after action
