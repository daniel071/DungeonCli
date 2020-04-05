#include <stdio.h>


int main() {
	char input[64];
	while(1) {
		printf("input> ");
		fgets(input, 64, stdin);
		printf("you entered %s\n", input);
	}
}

