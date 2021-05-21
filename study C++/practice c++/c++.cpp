#include <iostream>
#include <string.h>
using namespace std;
//strncmp, strcpy, strncat
int main() {
	char str[80] = { 0, }; //기존 문자열
	char find[10] = { 0, }; //찾을 문자열
	char change[10] = { 0, }; //바꿀 문자열
	char* first;
	char* last;
	char temp[80] = { 0, };
	cin.getline(str, 80); //getline은 띄어쓰기까지 배열에 포함하여 받아오기
	cin.getline(find, 10);
	cin.getline(change, 10);

	for (int i = 0; i < strlen(str); i++) { //str배열 전체 훑어보기
		first = &str[i];
		if(strncmp(first, find, sizeof(find))==0){
			//바꾸는 코드
			last = &str[i];
			strcpy(last, change);
			memset(temp, NULL, sizeof(temp)); //임시 배열 초기화
		}
	}
	cout << str << endl;
	return 0;
}
