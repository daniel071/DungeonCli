# Add to compile executables for each OS, so that Python isn't required
# python DungeonCli.py
python -m nuitka --follow-imports DungeonCli.py
