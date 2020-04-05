#include <stdio.h>

int main() {
	char input[64];
	// This is a comment
	// I have no idea what I am doing - Daniel who uses Python
	printf("input> ");
	fgets(input, 64, stdin);
	printf("entered %s! \n", input);
}
