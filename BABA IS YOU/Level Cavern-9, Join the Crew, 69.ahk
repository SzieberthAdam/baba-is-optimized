#NoEnv  ; Recommended for performance and compatibility with future AutoHotkey releases.
; #Warn  ; Enable warnings to assist with detecting common errors.
SendMode Input  ; Recommended for new scripts due to its superior speed and reliability.
SetWorkingDir %A_ScriptDir%  ; Ensures a consistent starting directory.

KeyDownTime = 25
LongKeyDownTime = 50
BabaStepRelax = 175
BabaLevelLoadApproxTime = 5000
BabaInitialRelax = 4000
NotYouRelax = 4000
TeleportRelax = 0
WinRelax = 0

OBSStartRelax = 1000
OBSStopRelax = 2750

^b::

; Start OBS Recording
Send, {Ctrl down}
Send, {F9 down}
Sleep %LongKeyDownTime%
Send, {F9 up}
Send, {Ctrl up}

Sleep %OBSStartRelax%

; Show version
Send, {Ctrl down}
Send, {j down}
Sleep %KeyDownTime%
Send, {j up}
Send, {Ctrl up}
Sleep %BabaStepRelax%

Send, {Enter down}
Sleep %KeyDownTime%
Send, {Enter up}

Sleep %BabaLevelLoadApproxTime%

Sleep %BabaInitialRelax%



Send, {Left down}
Sleep %KeyDownTime%
Send, {Left up}
Sleep %BabaStepRelax%

Send, {Down down}
Sleep %KeyDownTime%
Send, {Down up}
Sleep %BabaStepRelax%

Send, {Down down}
Sleep %KeyDownTime%
Send, {Down up}
Sleep %BabaStepRelax%

Send, {Down down}
Sleep %KeyDownTime%
Send, {Down up}
Sleep %BabaStepRelax%

Send, {Down down}
Sleep %KeyDownTime%
Send, {Down up}
Sleep %BabaStepRelax%

Send, {Right down}
Sleep %KeyDownTime%
Send, {Right up}
Sleep %BabaStepRelax%

Send, {Right down}
Sleep %KeyDownTime%
Send, {Right up}
Sleep %BabaStepRelax%

Send, {Right down}
Sleep %KeyDownTime%
Send, {Right up}
Sleep %BabaStepRelax%

Send, {Down down}
Sleep %KeyDownTime%
Send, {Down up}
Sleep %BabaStepRelax%

Send, {Right down}
Sleep %KeyDownTime%
Send, {Right up}
Sleep %BabaStepRelax%

Send, {Up down}
Sleep %KeyDownTime%
Send, {Up up}
Sleep %BabaStepRelax%

Send, {Right down}
Sleep %KeyDownTime%
Send, {Right up}
Sleep %BabaStepRelax%

Send, {Right down}
Sleep %KeyDownTime%
Send, {Right up}
Sleep %BabaStepRelax%

Send, {Right down}
Sleep %KeyDownTime%
Send, {Right up}
Sleep %BabaStepRelax%

Send, {Right down}
Sleep %KeyDownTime%
Send, {Right up}
Sleep %BabaStepRelax%

Send, {Up down}
Sleep %KeyDownTime%
Send, {Up up}
Sleep %BabaStepRelax%

Send, {Up down}
Sleep %KeyDownTime%
Send, {Up up}
Sleep %BabaStepRelax%

Send, {Left down}
Sleep %KeyDownTime%
Send, {Left up}
Sleep %BabaStepRelax%

Send, {Left down}
Sleep %KeyDownTime%
Send, {Left up}
Sleep %BabaStepRelax%

Send, {Left down}
Sleep %KeyDownTime%
Send, {Left up}
Sleep %BabaStepRelax%

Send, {Down down}
Sleep %KeyDownTime%
Send, {Down up}
Sleep %BabaStepRelax%

Send, {Down down}
Sleep %KeyDownTime%
Send, {Down up}
Sleep %BabaStepRelax%

Send, {Left down}
Sleep %KeyDownTime%
Send, {Left up}
Sleep %BabaStepRelax%

Send, {Left down}
Sleep %KeyDownTime%
Send, {Left up}
Sleep %BabaStepRelax%

Send, {Left down}
Sleep %KeyDownTime%
Send, {Left up}
Sleep %BabaStepRelax%

Send, {Left down}
Sleep %KeyDownTime%
Send, {Left up}
Sleep %BabaStepRelax%

Send, {Down down}
Sleep %KeyDownTime%
Send, {Down up}
Sleep %BabaStepRelax%

Send, {Up down}
Sleep %KeyDownTime%
Send, {Up up}
Sleep %BabaStepRelax%

Send, {Left down}
Sleep %KeyDownTime%
Send, {Left up}
Sleep %BabaStepRelax%

Send, {Down down}
Sleep %KeyDownTime%
Send, {Down up}
Sleep %BabaStepRelax%

Send, {Left down}
Sleep %KeyDownTime%
Send, {Left up}
Sleep %BabaStepRelax%

Send, {Left down}
Sleep %KeyDownTime%
Send, {Left up}
Sleep %BabaStepRelax%

Send, {Left down}
Sleep %KeyDownTime%
Send, {Left up}
Sleep %BabaStepRelax%

Send, {Left down}
Sleep %KeyDownTime%
Send, {Left up}
Sleep %BabaStepRelax%

Send, {Up down}
Sleep %KeyDownTime%
Send, {Up up}
Sleep %BabaStepRelax%

Send, {Up down}
Sleep %KeyDownTime%
Send, {Up up}
Sleep %BabaStepRelax%

Send, {Up down}
Sleep %KeyDownTime%
Send, {Up up}
Sleep %BabaStepRelax%

Send, {Right down}
Sleep %KeyDownTime%
Send, {Right up}
Sleep %BabaStepRelax%

Send, {Right down}
Sleep %KeyDownTime%
Send, {Right up}
Sleep %BabaStepRelax%

Send, {Right down}
Sleep %KeyDownTime%
Send, {Right up}
Sleep %BabaStepRelax%

Send, {Right down}
Sleep %KeyDownTime%
Send, {Right up}
Sleep %BabaStepRelax%

Send, {Right down}
Sleep %KeyDownTime%
Send, {Right up}
Sleep %BabaStepRelax%

Send, {Right down}
Sleep %KeyDownTime%
Send, {Right up}
Sleep %BabaStepRelax%

Send, {Right down}
Sleep %KeyDownTime%
Send, {Right up}
Sleep %BabaStepRelax%

Send, {Down down}
Sleep %KeyDownTime%
Send, {Down up}
Sleep %BabaStepRelax%

Send, {Down down}
Sleep %KeyDownTime%
Send, {Down up}
Sleep %BabaStepRelax%

Send, {Down down}
Sleep %KeyDownTime%
Send, {Down up}
Sleep %BabaStepRelax%

Send, {Down down}
Sleep %KeyDownTime%
Send, {Down up}
Sleep %BabaStepRelax%

Send, {Up down}
Sleep %KeyDownTime%
Send, {Up up}
Sleep %BabaStepRelax%

Send, {Right down}
Sleep %KeyDownTime%
Send, {Right up}
Sleep %BabaStepRelax%

Send, {Up down}
Sleep %KeyDownTime%
Send, {Up up}
Sleep %BabaStepRelax%

Send, {Up down}
Sleep %KeyDownTime%
Send, {Up up}
Sleep %BabaStepRelax%

Send, {Up down}
Sleep %KeyDownTime%
Send, {Up up}
Sleep %BabaStepRelax%

Send, {Left down}
Sleep %KeyDownTime%
Send, {Left up}
Sleep %BabaStepRelax%

Send, {Up down}
Sleep %KeyDownTime%
Send, {Up up}
Sleep %BabaStepRelax%

Send, {Right down}
Sleep %KeyDownTime%
Send, {Right up}
Sleep %BabaStepRelax%

Send, {Up down}
Sleep %KeyDownTime%
Send, {Up up}
Sleep %BabaStepRelax%

Send, {Right down}
Sleep %KeyDownTime%
Send, {Right up}
Sleep %BabaStepRelax%

Send, {Down down}
Sleep %KeyDownTime%
Send, {Down up}
Sleep %BabaStepRelax%

Send, {Down down}
Sleep %KeyDownTime%
Send, {Down up}
Sleep %BabaStepRelax%

Send, {Down down}
Sleep %KeyDownTime%
Send, {Down up}
Sleep %BabaStepRelax%

Send, {Down down}
Sleep %KeyDownTime%
Send, {Down up}
Sleep %BabaStepRelax%

Send, {Down down}
Sleep %KeyDownTime%
Send, {Down up}
Sleep %BabaStepRelax%

Send, {Right down}
Sleep %KeyDownTime%
Send, {Right up}
Sleep %BabaStepRelax%

Send, {Right down}
Sleep %KeyDownTime%
Send, {Right up}
Sleep %BabaStepRelax%

Send, {Right down}
Sleep %KeyDownTime%
Send, {Right up}
Sleep %BabaStepRelax%

Send, {Right down}
Sleep %KeyDownTime%
Send, {Right up}
Sleep %BabaStepRelax%

Send, {Right down}
Sleep %KeyDownTime%
Send, {Right up}
Sleep %BabaStepRelax%

Sleep %WinRelax%

Send, {Up down}
Sleep %KeyDownTime%
Send, {Up up}
Sleep %BabaStepRelax%



Sleep %OBSStopRelax%

; Stop OBS Recording
Send, {Ctrl down}
Send, {F10 down}
Sleep %LongKeyDownTime%
Send, {F10 up}
Send, {Ctrl up}



return