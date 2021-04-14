#include <iostream>
using namespace std;

void swap(int *x, int *y);

int main() {
	int a, b;
	cin >> a >> b;

	swap(&a, &b);

	cout << "a : " << a << endl;
	cout << "b : " << b << endl;

	return 0;
}

void swap(int *x, int *y) {
	int temp = *x;
	*x = *y;
	*y = temp;
}
