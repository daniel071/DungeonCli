#!/bin/bash

# Colours!!!
BLUE='\e[34m'
BOLD='\e[1m'
RESET='\033[0m'
NC='\e[39m'
GREEN='\e[32m'
YELLOW='\e[33m'
# Clean directory

if [ ! "~/.dungeoncli/" == "" ]; then
	# Directory exists

	echo -e "${BLUE}${BOLD}::${NC} Directory already exists!${RESET}"
	read -p "Do a clean install? (y/N) " -n 1 -r
	echo    # (optional) move to a new line
	if [[ $REPLY =~ ^[Yy]$ ]]
	then
		rm -rf ~/.dungeoncli/
	fi
mkdir ~/.dungeoncli/
fi

# Automatically fetch latest release - does not work yet!
# URL=$( curl -s "https://api.github.com/repos/daniel071/DungeonCli/releases/latest" \
#    | jq -r '.assets[] | select(.name=="DungeonCli-linux.zip") | .browser_download_url' )
# wget -O ~/.dungeoncli/dungeoncli.zip "$URL"

# Download binaries, .desktop files and icons
echo -e "\n${BLUE}${BOLD}::${NC} 1/3 Downloading binary${RESET}"
wget -q --show-progress -O ~/.dungeoncli/dungeoncli.zip https://github.com/daniel071/DungeonCli/releases/download/v0.6.0-beta/DungeonCli-linux.zip

echo -e "\n${BLUE}${BOLD}::${NC} 2/3 Downloading icon${RESET}"
wget -q --show-progress -O ~/.dungeoncli/dungeoncli.png https://raw.githubusercontent.com/daniel071/DungeonCli/master/Images/Logos/stableTerminal.png

echo -e "\n${BLUE}${BOLD}::${NC} 3/3 Downloading .desktop file${RESET}"
wget -q --show-progress -O ~/.dungeoncli/dungeoncli_old.desktop https://raw.githubusercontent.com/daniel071/DungeonCli/master/Scripts/dungeonCli.desktop

# Setup binary
echo -e "\n${BLUE}${BOLD}::${NC} Setting up binary${RESET}"
echo -e "${YELLOW}${BOLD} ->${RESET} Unzipping file"
unzip -q ~/.dungeoncli/dungeoncli.zip -d ~/.dungeoncli/dungeoncli
echo -e "${YELLOW}${BOLD} ->${RESET} Adding executable permission"
chmod +x ~/.dungeoncli/dungeoncli/DungeonCli-linux-v0.6.0/DungeonCli
echo -e "${YELLOW}${BOLD} ->${RESET} Removing old .desktop file if it exists"
rm ~/.dungeoncli/dungeonCli.desktop

# Replace relative paths with absolute paths
echo -e "\n${BLUE}${BOLD}::${NC} Setting up menu item${RESET}"
echo -e "${YELLOW}${BOLD} ->${RESET} Replacing relative paths with absolute ones"
sed "s|~|$HOME|g" ~/.dungeoncli/dungeoncli_old.desktop >> ~/.dungeoncli/dungeonCli.desktop

# Add a menu item so user can easily find it
echo -e "${YELLOW}${BOLD} ->${RESET} Installing .desktop file"
sudo desktop-file-install ~/.dungeoncli/dungeonCli.desktop

echo -e "\n${GREEN}${BOLD}Success!${RESET}"
