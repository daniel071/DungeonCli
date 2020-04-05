/*
DungeonCli is a terminal based program where you get to explore
places and earn coins. You can spend those coins on various items,
have fun!

Programming: Daniel, Xenthio
Dialogue: Bob
*/

#include <stdio.h>

int main() {
	char input[64];
	// This is a comment
	// I have no idea what I am doing - Daniel who uses Python
	printf("input> ");
	fgets(input, 64, stdin);
	printf("you entered %s\n", input);
}
