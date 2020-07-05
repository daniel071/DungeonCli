md bin.build
python -m nuitka --standalone --remove-output --output-dir=bin.build --file-reference-choice=runtime DungeonCli.py
copy .\Music .\bin.build\DungeonCli.dist\
copy .\Sounds .\bin.build\DungeonCli.dist\
echo the build is in .\bin.build\DungeonCli.dist\
pause
