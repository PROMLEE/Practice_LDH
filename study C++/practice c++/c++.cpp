#include <iostream>
using namespace std;

int main() {
	int row = 10, col = 10;
	int product[10][10] = {0};
	for (int i = 1; i < row; i++) {
		for (int j = 1; j < col; j++) {
			product[i][j] = i * j;
			cout << product[i][j]<<"\t";
		}
		cout << endl;
	}
	return 0;
}
