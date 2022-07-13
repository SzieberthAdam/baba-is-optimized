@echo off

:loop

python autobaba.py autobaba.txt autobaba-work-template.ahk

set /p "answer=< Enter to repeat, Q to quit >"

if /I [%answer%]==[q] goto end

goto loop

:end 