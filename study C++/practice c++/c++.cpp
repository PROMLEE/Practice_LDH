#include <iostream>
#include <string.h>
using namespace std;
//strncmp, strcpy, strncat
int main() {
	char str[80] = { 0, }; //���� ���ڿ�
	char find[10] = { 0, }; //ã�� ���ڿ�
	char change[10] = { 0, }; //�ٲ� ���ڿ�
	char* first;
	char* last;
	char temp[80] = { 0, };
	cin.getline(str, 80); //getline�� ������� �迭�� �����Ͽ� �޾ƿ���
	cin.getline(find, 10);
	cin.getline(change, 10);

	for (int i = 0; i < strlen(str); i++) { //str�迭 ��ü �Ⱦ��
		first = &str[i];
		if(strncmp(first, find, sizeof(find))==0){
			//�ٲٴ� �ڵ�
			last = &str[i];
			strcpy(last, change);
			memset(temp, NULL, sizeof(temp)); //�ӽ� �迭 �ʱ�ȭ
		}
	}
	cout << str << endl;
	return 0;
}
