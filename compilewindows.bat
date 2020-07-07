md bin.build
python -m nuitka --standalone --remove-output --show-progress --show-scons --output-dir=bin.build --file-reference-choice=runtime DungeonCli.py
copy .\Music .\bin.build\DungeonCli.dist\Music\
copy .\Sounds .\bin.build\DungeonCli.dist\Sounds\
echo the build is in .\bin.build\DungeonCli.dist\
pause
