@echo off
rem https://www.computerhope.com/issues/ch000820.htm#windows

if [%1]==[] goto default

:arged

find /v /c "&*fake&*" %1

set /p "answer=< Enter to repeat, Q to quit >"

if /I [%answer%]==[q] goto end

goto arged

:default

find /v /c "&*fake&*" autobaba.txt

set /p "answer=< Enter to repeat, Q to quit >"

if /I [%answer%]==[q] goto end

goto default

:end 