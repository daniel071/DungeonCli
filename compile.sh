#!/bin/bash

mkdir bin.build
python3 -m nuitka --standalone --remove-output --show-progress --show-scons --output-dir=bin.build --file-reference-choice=runtime DungeonCli.py
if [[ "$OSTYPE" == "darwin"* ]]; then
	mv ./DungeonCli.bin ./bin.build/DungeonCli_osx
	sudo codesign -f -s - ./bin.build/DungeonCli.dist/Python
elif [[ "$OSTYPE" == "linux-gnu" ]]; then
	mv ./DungeonCli.bin ./bin.build/DungeonCli_linux
else
	mv ./DungeonCli.bin ./bin.build/DungeonCli
fi

cp -r ./Music ./bin.build/DungeonCli.dist/
cp -r ./Sounds ./bin.build/DungeonCli.dist/

zip DungeonCli.zip ./bin.build/DungeonCli.dist/
