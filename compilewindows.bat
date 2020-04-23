md bin.build
python -m nuitka --follow-imports --plugin-enable=multiprocessing DungeonCli.py
move .\DungeonCli.exe .\bin.build\DungeonCli
pause
