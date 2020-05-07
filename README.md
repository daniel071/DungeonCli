"In need of coins, eh? I mean i could let you have some of my precious coins, but ya gotta know the secret code" - Money Grinch
# DungeonCli
**What is it?**

DungeonCli is a terminal based program where you get to explore
places and earn coins. You can spend those coins on various items,
have fun!

##### Note: There is also a swift rewrite (depreciated)
There is another depreciated version, made with swift at the `swift-rewrite` branch


## Installation:
### From binaries
**(Recommended method)**

#### On windows:
Download the .exe file from the releases page and run it.

#### On *nix based systems:
1. Go to the releases page and download the binary for your operating system
2. Give the binary executable permissions and run it

**On Linux:**
Give it priviledges with `chmod +X ./DungeonCli_Linux` then run it with
`./DungeonCli_Linux`

**On MacOS:**
Give it priviledges with `chmod +X ./DungeonCli_osx` then run it with
`./DungeonCli_osx`


---


### With Python
You **MUST** have ffmpeg installed in order for the music to work. On MacOS and Linux it should be already installed, if not, please use your package manager.

##### How to install ffmpeg in windows:
1. Download the build from here:
https://ffmpeg.zeranoe.com/builds/win64/static/ffmpeg-4.2.2-win64-static.zip
2. Extract the zip somewhere and copy the `\bin` directory
3. Add that directory to your path, if you don't know how to,
Search 'path' in the start menu and press 'enter' -> Click on 'Environment variables' -> On System Variables, click on 'Path' and click 'Edit' -> Click 'New' and paste in the directory -> Click OK on everything -> **RESTART**


##### How to install DungeonCli:
1. Download the .zip file and extract it or type

	`git clone http://119.17.132.38:3000/Daniel/DungeonCli.git`
2. Make sure you have Python 3.8.2 installed. If you don't, you
can install it from www.python.org
3. Make sure you have the dependencies installed with `pip install -r requirements.txt`
4. Open the terminal in the directory and type `python DungeonCli.py`


---


## Compiling:
**(Only for experienced users!)**

1. Download the .zip file and extract it or type

	`git clone http://119.17.132.38:3000/Daniel/DungeonCli.git`
2. Make sure you have the dependencies installed. These include:
- Python 3.8.2 (https://www.python.org/downloads/)
- Nuitka (https://nuitka.net/pages/download.html)
- Mingw (https://osdn.net/projects/mingw/releases/)
3. Run the compile script:

	If you're on Linux / Unix, make sure to give compile.sh executable
priviledges with `chmod +X ./compile.sh` then run it with `./compile.sh`
If you're on Windows, run `compilewindows.bat`


---


## Screenshots:
**The start screen**

![The start screen](http://119.17.132.38:3000/Daniel/DungeonCli/raw/branch/master/Screenshots/v0.3.1%20Start%20Screen.png)

**Common commands**

![Common commands](http://119.17.132.38:3000/Daniel/DungeonCli/raw/branch/master/Screenshots/v0.3.1%20common%20commands.png)

**Healing**

![Healing](http://119.17.132.38:3000/Daniel/DungeonCli/raw/branch/master/Screenshots/v0.3.1%20healing.png)

**The combat system**

![The combat system](http://119.17.132.38:3000/Daniel/DungeonCli/raw/branch/master/Screenshots/combat%20system%20v0.3.1.png)

**The Store**

![The Store](http://119.17.132.38:3000/Daniel/DungeonCli/raw/branch/master/Screenshots/v0.3.0%20store.png)

---

## Usage:
Type 'h' or 'help' to get a help screen

<br>

## Contributing:
If you would like to make a change to the code, you can fork this, make changes
to it and then submit a pull request. @Xenthio and @Daniel can check your pull
request and merge it if it's good.

If you are experiencing a bug, you can open up an issue and we will try and help
fix it.

#### Don't know how to code?
You can always help with translations, currently, they are not implemented
but if you are interested in helping translate a language, we will implement
that. If you want to translate, just let us know by opening up an issue.

<br>

## To Do!
- [ ] Neat and text based engine.
- [x] Make text easy to read by having it scan in.
- [ ] Convince Daniel to use threads (I do want to use threads!! I can't figure out how to kill threads tho!!)
- [ ] Write more story
- [x] Basic Gameplay mechanics
- [ ] Real 'bin' format save files. not the fake stuff.
- [x] Overhaul the combat system, add sparing and using items
- [x] Fix combat system dealing no damage
- [ ] Make extra swords that deal extra damage
- [ ] Add more Armour which absorbs a percentage of damage
- [x] Fix bug where if you die while in combat, the combat function persists
- [ ] Add critical shots, where there is a chance that you can get double the damage

<br>

## What to do next?
Congratulations! You got to the end, perhaps you'd like to join the official
discord server?

https://discord.gg/eAUqKKe
