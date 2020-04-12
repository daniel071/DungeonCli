
md .Builds
python3 -m nuitka --follow-imports DungeonCli.py
move ./DungeonCli.exe ./.Builds/DungeonCli