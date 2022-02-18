#include<iostream>
using namespace std;

int func(int);
int num = 10;
int main() {
	int num; num = 5;
	cout << num;
	cout << func(num);
	return 0;
}
int func(int x) {
	return num;
}