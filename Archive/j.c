#include <stdio.h>

char* Inv[] = {"0 x Braincells", "0 x Skills"};

int main() {
	char input[64];
	int coins = 0; // Fucking poor cunt lmao.

	char * intro = "you are some faggot who cant program, type a b or c";
	char introchoices[] = {"a","b","c"};
	printf(intro);
	printf("input> ");
	fgets(input, 64, stdin);
	printf("you entered %s\n", input);
	// This is a comment
	// I have no idea what I am doing - Daniel who uses Python
	
	while(1) {
		printf("input> ");
		fgets(input, 64, stdin);
		printf("you entered %s\n", input);
	}
}

void initInventory() {
	
}
void openInventory() {
	printf(Inv);
}