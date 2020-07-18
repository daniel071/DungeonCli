# Contributing on DungeonCli
Thanks for deciding to contribute to DungeonCli!

## Translations
If you want to add translations, please open up an issue
and we will implement it in.

## How to make a pull request
You can create a fork of this, create changes to the fork and then open a
pull request, and one of the maintainers will review your code. If it's
good we'll accept it.

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

#### /Engine/ Directory
In /Engine/, the core functions of DungeonCli are stored. This includes
the combat system, the text system, the potion system and variables for
the scene and the player.

#### /src/ Directory
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
in the [Discord server](https://discord.gg/eAUqKKe) or Daniel071 on IRC (Freenode)
