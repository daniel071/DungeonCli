### NOTE:
You **MUST** have ffmpeg installed in order for the music to work. On MacOS and Linux it should be already installed, if not, please use your package manager. **Windows does not come with ffmpeg preinstalled however,
I have created an installation script that will do install it for you. It is built in to
DungeonCli.py**

---

### From binaries
**(Recommended method)**

#### On Windows:
Download the .exe file from the releases page and run it.

#### On Unix based systems:
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