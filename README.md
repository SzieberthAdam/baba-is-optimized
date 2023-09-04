# BABA IS OPTIMIZED – Baba Is You (Outdated) Optimized Solutions & Walkthrough

The original goal of this repo is to store the shortest known solutions and walkthrough of Baba Is You, which is a puzzle video game created by Finnish indie developer Arvi Teikari aka. Hempuli.

The optimizer community is in the [channel-is-full-game-spoilers/min-steps-routing thread](https://discord.com/channels/556333985882439680/878875784041865236).

Some videos made with this tool and AutoHotkey and OBS Studio:
https://www.youtube.com/playlist?list=PL2Qu4Gqa0Mog2g3XkWth-2RD7787K4rj5

*Archived as I am not committed enough to maintain it. -- SzieberthAdam*

Levelpacks
----------

* [Baba Is You](BABA%20IS%20YOU)


autobaba
--------

Autobaba is not a levelpack but a toolbar to note, test, and publish solutions.
I use these tools for my minimum steps routing workflow.


Solution Format
-------------------------

Example:

```
LD4R2D-RU2DR3-U6RUL-ULD6L-DL6DR6-DRUW-U10
```

* `-`: used optionally for better readability (4 sequence grouping is recommended)
* `number`: number of repetitions of the previous action (1 excluded)
* `U`: up
* `D`: down
* `L`: left
* `R`: right
* `W`: wait (space key)
* `X`: Exit to Map
* `Z`: Reset

Thus, the above example transfers to:

```
left, down, down, down, down, right, right, down,
right, up, up, down, right, right, right,
up, up, up, up, up, up, right, up, left,
up, left, down, down, down, down, down, down, left,
down, left, left, left, left, left, left, down, right, right, right, right, right, right,
down, right, up, wait,
up, up, up, up, up, up, up, up, up, up
```
