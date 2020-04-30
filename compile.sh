#!/bin/bash

mkdir bin.build
python3 -m nuitka --follow-imports --plugin-enable=multiprocessing DungeonCli.py
if [[ "$OSTYPE" == "darwin"* ]]; then
	mv ./DungeonCli.bin ./bin.build/DungeonCli_osx
elif [[ "$OSTYPE" == "linux-gnu" ]]; then
	mv ./DungeonCli.bin ./bin.build/DungeonCli_linux
else
	mv ./DungeonCli.bin ./bin.build/DungeonCli
fi
