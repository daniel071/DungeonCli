### NOTE:
You **MUST** have ffmpeg installed in order for the music to work. On MacOS and Linux it should be already installed, if not, please use your package manager. **Windows does not come with ffmpeg preinstalled however,
I have created an installation script that will do install it for you. It is built in to
DungeonCli.py**

<br>

### From binaries
**(Recommended method)**

##### There are 2 different places where you can download binaries.

[Stable builds](http://pavela.net:3000/Daniel/DungeonCli/releases) ![image](http://pavela.net:3000/Daniel/DungeonCli/raw/branch/master/Images/Logos/stableTerminal.png)| [Nightly builds](http://pavela.net:8090/blue/organizations/jenkins/DungeonCI/activity) ![image](http://pavela.net:3000/Daniel/DungeonCli/raw/branch/master/Images/Logos/nightlyTerminal.png)
------------ | -------------
<img src="https://upload.wikimedia.org/wikipedia/commons/5/5f/Windows_logo_-_2012.svg" alt="Windows 10 Logo" width="100"/> <img src="https://upload.wikimedia.org/wikipedia/commons/a/af/Tux.png" alt="Linux Logo" width="100"/> <img src="https://upload.wikimedia.org/wikipedia/commons/2/22/MacOS_logo_%282017%29.svg" alt="MacOS Logo" width="100"/>| <img src="https://upload.wikimedia.org/wikipedia/commons/a/af/Tux.png" alt="Linux Logo" width="100"/> <img src="https://upload.wikimedia.org/wikipedia/commons/2/22/MacOS_logo_%282017%29.svg" alt="MacOS Logo" width="100"/>
Stable builds are major milestones that are not released frequently. <br>These have been manually compiled and have been tested to work. | Nightly builds are released every day. They have the latest updates however, are not tested. <br>NOTE: Currently we only have Linux and MacOS nightly builds. <br>Windows builds will be available as soon as we get a Windows server.



#### On Windows:
Download the Windows .zip file, extract it and run *DungeonCli.exe*
##### NOTE: Make sure to keep the exe file in the folder it came with otherwise it won't run!

#### On Unix based systems:
1. Download the binary for your operating system
2. Give the binary executable permissions and run it

**On Linux/MacOS:**
Give it priviledges with `chmod +X ./DungeonCli` then run it with
`./DungeonCli_Linux`

<br>

---


### With Python

##### How to install DungeonCli:
1. Download the .zip file and extract it or type

	`git clone http://119.17.132.38:3000/Daniel/DungeonCli.git`
2. Make sure you have Python 3.8.2 installed. If you don't, you
can install it from https://www.python.org
3. Make sure you have the dependencies installed with `pip install -r requirements.txt`
4. Open the terminal in the directory and type `python DungeonCli.py`

<br>

---


## Compiling:
**(Only for experienced users!)**

1. Download the .zip file and extract it or type

	`git clone http://119.17.132.38:3000/Daniel/DungeonCli.git`
2. Make sure you have the dependencies installed. These include:
- [Python 3.8.2](https://www.python.org/downloads/)
- [Nuitka](https://nuitka.net/pages/download.html)
- [MinGW](https://osdn.net/projects/mingw/releases/) (Only required on Windows)
3. Run the compile script:

	If you're on Linux / Unix, make sure to give compile.sh executable
priviledges with `chmod +X ./compile.sh` then run it with `./compile.sh`
If you're on Windows, run `compilewindows.bat`
