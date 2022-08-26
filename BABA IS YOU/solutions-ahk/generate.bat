@echo off
for %%f in (..\solutions-multiline\*.txt) do (
echo %%f
python ..\..\autobaba\autobaba.py "%%f" ..\..\autobaba\autobaba-template.ahk
move "..\solutions-multiline\%%~nf.ahk" "%%~nf.ahk"
)
echo Done.
