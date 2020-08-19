#!/bin/bash

mkdir ~/.dungeoncli/

wget -O ~/.dungeoncli/dungeoncli.zip https://git.pavela.net/attachments/9ba2e156-5732-4357-a641-269c25741f27
wget -nv -O ~/.dungeoncli/dungeoncli.png https://git.pavela.net/Daniel/DungeonCli/raw/branch/master/Images/Logos/stableTerminal.png
wget -nv -O ~/.dungeoncli/dungeoncli_old.desktop https://git.pavela.net/Daniel/DungeonCli/raw/branch/master/Scripts/dungeonCli.desktop

unzip ~/.dungeoncli/dungeoncli.zip -d ~/.dungeoncli/dungeoncli
chmod +x ~/.dungeoncli/dungeoncli/DungeonCli-linux-v0.6.0/DungeonCli
rm ~/.dungeoncli/dungeonCli.desktop

sed "s|~|$HOME|g" ~/.dungeoncli/dungeoncli_old.desktop >> ~/.dungeoncli/dungeonCli.desktop
sudo desktop-file-install ~/.dungeoncli/dungeonCli.desktop
