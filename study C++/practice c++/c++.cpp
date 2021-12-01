#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <fstream>
#include <cstring>
using namespace std;

int len(char* n);
int findword(char* n);
int main() {
	int alphabet[26] = { 0, };
	ifstream myfile;
	myfile.open("data/example.txt");
	char arr[10][500];
	int i = -1;
	while (myfile) {
		i++;
		myfile.getline(arr[i], 500);
	}
	myfile.close();
	for (int j = 0; j < i; j++) {
		for (int k = 0; k < len(arr[j]); k++) {
			if ((arr[j][k] >= 65) & (arr[j][k] <= 90))
				alphabet[arr[j][k] - 65] += 1;
			else if ((arr[j][k] >= 97) & (arr[j][k] <= 121))
				alphabet[arr[j][k] - 97] += 1;
		}
	}
	int count = 0, x;
	for (int i = 0; i < 26; i++) {
		if (alphabet[i] > count) {
			x = i;
			count = alphabet[i];
		}
	}
	char* temp;
	char X;
	int a;
	for (int j = 0; j < i; j++) {
		a = findword(arr[j]);
		temp = strtok(arr[j], " ");
		for (int k = 1; k <=a; k++) {
			for (int l = 0; l < len(temp); l++) {
				if ((temp[l] - 65 == x) || (temp[l] - 97 == x)) {
					cout << temp << endl;
					break;
				}
			}
			temp = strtok(NULL, " ");
		}
	}
	return 0;
}
int len(char* n) {
	int x;
	for (x = 0; n[x]; x++);
	return x;
}
int findword(char* n) {
	int a = 0, x = len(n);
	for (int i = 0; i < x; i++) {
		if (n[i] == ' ')
			a++;
	}
	a++;
	return a;
}