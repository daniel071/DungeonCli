### NOTE:
You **MUST** have ffmpeg installed in order for the music to work. On MacOS and Linux it should be already installed, if not, please use your package manager. **Windows does not come with ffmpeg preinstalled however,
I have created an installation script that will do install it for you. It is built in to
DungeonCli.py**

<br>

### From binaries
**(Recommended method)**

##### There are 2 different places where you can download binaries.

‎| [Stable builds <br> <img src="https://raw.githubusercontent.com/daniel071/DungeonCli/master/Images/Logos/stableTerminal.png" alt="Logo" width="150"/>](https://github.com/daniel071/DungeonCli/releases)  | [Nightly builds <br> <img src="https://raw.githubusercontent.com/daniel071/DungeonCli/master/Images/Logos/nightlyTerminal.png" alt="Logo" width="150"/>](https://jenkins.pavela.net/blue/organizations/jenkins/DungeonCI/activity) |
---            |         :-: |      :-:     |
Stability      | ✔️           | ❌
Latest Updates | ❌          | ✔️
Windows Builds | ✔️           | ❌
MacOS Builds   | ✔️           | ✔️
Linux Builds   | ✔️           | ✔️

#### On Windows:
Download the Windows .zip file, extract it and run *DungeonCli.exe*
##### NOTE: Make sure to keep the exe file in the folder it came with otherwise it won't run!

#### On Linux:
I have created an installation script that will automatically install DungeonCli.
Simply Run:

```bash
curl -s https://raw.githubusercontent.com/daniel071/DungeonCli/master/Scripts/install-linux.sh | sh
```
###### **NOTE: Root priviledges will be requested in the script as it is required to write to /usr/share/applications**/

#### On macOS:
1. Download the binary for your operating system
2. Give the binary executable permissions with `chmod +x ./DungeonCli`
3. Run it with `./DungeonCli`

<br>

---


### With Python

##### How to install DungeonCli:
1. Download the .zip file and extract it or type

	`git clone https://github.com/daniel071/DungeonCli.git`
2. Make sure you have Python 3.8.2 installed. If you don't, you
can install it from https://www.python.org
3. Make sure you have the dependencies installed with `pip install -r requirements.txt`
4. Open the terminal in the directory and type `python DungeonCli.py`

<br>

---


## Compiling:
**(Only for experienced users!)**

1. Download the .zip file and extract it or type

	`git clone https://github.com/daniel071/DungeonCli.git`
2. Make sure you have the dependencies installed. These include:
- [Python 3.8.2](https://www.python.org/downloads/)
- [Nuitka](https://nuitka.net/pages/download.html)
- [MinGW](https://osdn.net/projects/mingw/releases/) (Only required on Windows)
3. Run the compile script:

	If you're on Linux / Unix, make sure to give compile.sh executable
priviledges with `chmod +X ./compile.sh` then run it with `./compile.sh`
If you're on Windows, run `compilewindows.bat`
