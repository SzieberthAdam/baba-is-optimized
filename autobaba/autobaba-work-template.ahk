﻿#NoEnv  ; Recommended for performance and compatibility with future AutoHotkey releases.
; #Warn  ; Enable warnings to assist with detecting common errors.
SendMode Input  ; Recommended for new scripts due to its superior speed and reliability.
SetWorkingDir %A_ScriptDir%  ; Ensures a consistent starting directory.


KeyDownTime = 40
BabaStepRelax = 80
NotYouRelax = 0
TeleportRelax = 0
WinRelax = 0



^r::  ; Ctrl+R

Sleep 250
Reload
Send, {r down}
Sleep %KeyDownTime%
Send, {r up}



^b::  ; Ctrl+B



{{baba}}



return