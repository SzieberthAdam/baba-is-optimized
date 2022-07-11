@echo off
rem https://www.computerhope.com/issues/ch000820.htm#windows

if [%1]==[] goto default

find /v /c "&*fake&*" %1

pause

goto :eof

:default

find /v /c "&*fake&*" autobaba.txt

pause
