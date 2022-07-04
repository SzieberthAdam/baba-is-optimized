#NoEnv  ; Recommended for performance and compatibility with future AutoHotkey releases.
; #Warn  ; Enable warnings to assist with detecting common errors.
SendMode Input  ; Recommended for new scripts due to its superior speed and reliability.
SetWorkingDir %A_ScriptDir%  ; Ensures a consistent starting directory.


KeyDownTime = 25
BabaStepRelax = 100
BabaLevelReloadApproxTime = 500
NotYouRelax = 0
TeleportRelax = 0
WinRelax = 0

^!r::Reload  ; Ctrl+Alt+R

^b::

Send, {Ctrl down}
Send, {r down}
Sleep %KeyDownTime%
Send, {r up}
Send, {Ctrl up}
Sleep %BabaLevelReloadApproxTime%



{{baba}}



return