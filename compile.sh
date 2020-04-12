# Add to compile executables for each OS, so that Python isn't required
# python DungeonCli.py
mkdir .Builds
python3 -m nuitka --follow-imports DungeonCli.py
if [[ "$OSTYPE" == "darwin"* ]]; then
	mv ./DungeonCli.bin ./.Builds/DungeonCli_osx
elif [[ "$OSTYPE" == "linux-gnu" ]]; then
	mv ./DungeonCli.bin ./.Builds/DungeonCli_linux
else
	mv ./DungeonCli.bin ./.Builds/DungeonCli
fi
