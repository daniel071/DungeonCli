# Contributing on DungeonCli
Thanks for deciding to contribute to DungeonCli!

## Translations
You can always help with translations, currently, they are not implemented
but if you are interested in helping translate a language, we will implement
that. If you want to translate, just let us know by opening up an issue.

## How to make a pull request
You can create a fork of this, create changes to the fork and then open a
pull request, and one of the maintainers will review your code. If it's
good we'll accept it.

## Documentation
Documentation is used to help provide reference and instructions on how
to do things and what things are. This includes both internal in-code
comments and external .MD files such as this one. You can help by
adding more information.

## Programming
If you want to add an extra feature make sure to test your code before
opening a pull request.

Please try and use Python PEP8 styling and camelCase for variables, functions
and class names. Use intuitive names and make sure that your
feature doesn't break anything else. Try to include code comments in
your code so others can understand it easier.

For people with write permission to the master branch, feel free to
commit directly to master for small changes and bug fixes however,
if you are adding a major feature or update, it is recommended to
create a pull request instead so others can review your code.

## Some useful stuff
Some of our code comments may help with you understanding the code, some may not.
Here is a explanation of some main parts:

### Our build server
Available at https://jenkins.pavela.net/, you can access all previous builds
and build logs for any reference. If you have any DungeonCli related tool
that needs builds, [contact us](#Contact)

### The Game Folder
Recently implemented, all core game code has been moved to the `Game` folder.
Files regarding the engine, scenes, events and more is stored here.

**Within the Game folder**

##### /Game/Engine/ Directory
In /Engine/, the core functions of DungeonCli are stored. This includes
the combat system, the text system, the potion system and variables for
the scene and the player.

##### /Game/Scenes/ Directory
*This feature is still in development. You can help by improving it.*

In /Game/Scenes/, custom scenes can be placed and be read within the game.
Checkout [`SceneExample.py`](Game/Scenes/SceneExample.py) for reference
on how to use it.

#### /src/ Directory
*This folder will soon be moved to the /Game/ folder*

In /src/, several other stuff that isn't part of the core engine is included.
Currently `saveSystem.py` is unused, `multiplayer.py` is unfinished and
`richPrecense.py` is used for the Discord Rich Precense when playing the game.

#### main()
The function that asks for a command and then runs another function based on
the command typed.

#### start()
This is where all the scenes and story happens.

## Contact
If you would like an explanation about something in the code, you can ask us
in the [Discord server](https://discord.gg/eAUqKKe) or Daniel071 on IRC (libera.chat) (RIP Freenode)
