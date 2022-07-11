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

1. Start *Baba Is You* in windowed mode (fullscreen off)
2. Open `autobaba.txt` with *Notepad*
3. Start solving a level using the correct [format](https://github.com/SzieberthAdam/baba-is-you-solutions#solution-format). Note down only some several actions at a time then continue with the next point.
4. Save `autobaba.txt`.
5. Run `autobaba-work.bat`. It will update your `autobaba.ahk` file.
6. For the first time, run `autobaba.ahk`. An *AutoHotkey* icon should appear in your system tray: ![AutoHotkey Tray Icon](https://raw.githubusercontent.com/SzieberthAdam/baba-is-you-solutions/master/autobaba/img/AHK-Icon5.png). If *AutoHotkey* is already running, right click on the icon and choose *Reload This Script*. During the work process, you can also reload by pressing `Ctrl+Alt+R`.
7. Make *Baba Is You* the active window and reload the level with the `R` key.
8. Run your macro by pressing `Ctrl+B`. You should see your solution replayed live on screen.
9. If the level is not yet won then go back to point 3. If won then run `autobaba.bat` which creates your final `autobaba.ahk`.
10. Copy and rename `autobaba.txt` and `autobaba.ahk` files to a safe place. I recommend using my name format: `Level Cavern-11, Trick Door, 114.txt` and `Level Cavern-11, Trick Door, 114.ahk`. Here the solution was done in 114 time units. To get the number of time units of `autobaba.txt`, run the `linecount.bat` batch file.
11. Finally, run `reset.bat` to clean up `autobaba.txt` and `autobaba.ahk` files.


Video Making
------------

*Coming soon…*
