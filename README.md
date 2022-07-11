Baba Is You Solutions – *World Records*
=======================================

This site is dedicated to Baba Is You, which is a puzzle video game created by Finnish indie developer Arvi Teikari.
I keep track of the shortest solutions for the levels of the game.
Levelpacks are separated by subfolders.

autobaba
--------

Autobaba is not a levelpack but a toolbar to note, test, and publish solutions.


Format
------

The syntax of a solution is very simple:

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

This is the shortest solution to *Level 1: Where Do I Go?* done in 25 time units.
[Watch the solution by Alayric](https://youtu.be/42OOvZxvH6k).
You can count the lines one-by-one to get the time units the solution takes which is 25.
I rather recommend using a text editor which has line numbering to see how many.

### Actions

Only actions are required for a valid solution file. One action per line, one line per action!

* **U**: up
* **D**: down
* **L**: left
* **R**: right
* **. (period)**: wait (space key)

### Comments and Rule Changes

Solutions may contain comments in any action line and after a `#`.

Rule changes are a special type of comment.
By convention, rule changes start with a `-` or `+` character, separated by `;`, and are noted with upper case letters.
If you want rule changes and comment noted in the same line, start with rule changes and then put a second `#` to separate your comment properly, finally end with the comment.
*Always note every rule changes or none!*
Rule changes are useful for the solution viewer as it helps the pairing of the text and the video.

### Indicators

Indicators are optional.
They indicate special events which may require some extra wait time in the video solution.
Besides, they provide some extra anchors for the solution viewer with the pairing of the text and the video.

* **y**: indicates that YOU condition has been ended; put after action
* **t**: indicates a teleport trip; put after action
* **w**: indicates a win condition; put before action
