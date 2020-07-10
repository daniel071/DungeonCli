#!/bin/bash

mkdir bin.build
python3 -m nuitka --standalone --remove-output --show-progress --show-scons --output-dir=bin.build --file-reference-choice=runtime DungeonCli.py
if [[ "$OSTYPE" == "darwin"* ]]; then
	cp ./DungeonCli.bin ./bin.build/DungeonCli_osx
	sudo codesign -f -s - ./bin.build/DungeonCli.dist/Python
elif [[ "$OSTYPE" == "linux-gnu" ]]; then
	cp ./DungeonCli.bin ./bin.build/DungeonCli_linux
else
	cp ./DungeonCli.bin ./bin.build/DungeonCli
fi

cp -r ./Music ./bin.build/DungeonCli.dist/
cp -r ./Sounds ./bin.build/DungeonCli.dist/


if [[ "$OSTYPE" == "darwin"* ]]; then
	cp -r /Library/Frameworks/Python.framework ./bin.build/DungeonCli.dist/
	zip -r DungeonCli_MacOS.zip ./bin.build/DungeonCli.dist/
elif [[ "$OSTYPE" == "linux-gnu" ]]; then
	zip -r DungeonCli_Linux.zip ./bin.build/DungeonCli.dist/
else
	zip -r DungeonCli_Other.zip ./bin.build/DungeonCli.dist/
fi
