#include <stdio.h>
#define MAX 'z'

int main(void){
	char x='i';
	for (int i = MAX - x; i >= 0;i--) {
		//����
		for (int j = 0; j < i; j++)
			printf(" ");
		//~a
		for (int a = MAX-i ; a >= x; a--)
			printf("%c", a);
		//b~
		for (int b = x + 1; b <= MAX - i; b++)
			printf("%c", b);
		if (i != 0) 
			printf("\n");
	}
}
