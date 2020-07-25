#!/bin/bash

mkdir ~/.dungeoncli/
# wget -O ~/.dungeoncli/dungeoncli.zip http://pavela.net:3000/attachments/9ba2e156-5732-4357-a641-269c25741f27
wget -nv -O ~/.dungeoncli/dungeoncli.png http://pavela.net:3000/Daniel/DungeonCli/raw/branch/master/Images/Logos/stableTerminal.png
wget -nv -O ~/.dungeoncli/dungeoncli_old.desktop http://pavela.net:3000/Daniel/DungeonCli/raw/branch/master/Scripts/dungeonCli.desktop
wget -nv -O ~/.dungeoncli/start_game.sh http://pavela.net:3000/Daniel/DungeonCli/raw/branch/master/Scripts/start_game.sh
# unzip ~/.dungeoncli/dungeoncli.zip -d ~/.dungeoncli/dungeoncli
chmod +x ~/.dungeoncli/dungeoncli/DungeonCli-linux-v0.6.0/DungeonCli
sed "s|~|$HOME|g" ~/.dungeoncli/dungeoncli_old.desktop >> ~/.dungeoncli/dungeonCli.desktop
sudo desktop-file-install ~/.dungeoncli/dungeonCli.desktop
