//#include <iostream>
//using namespace std;
//
//void func();
//int main() {
//	int i, j;
//	int x[5] = { 2, 3, 4, 8, 9 };
//	int* ptr = &x[2];
//	i = (*ptr)++;
//	j = *ptr++;
//	cout << i<<endl;
//	cout << j;
//	return 0;
//}
//void func() {
//	int i = 3;
//	cout << i;
//	if (--i)
//		func();
//}
//#include <iostream>
//using namespace std;
//
//#define EVEN 0
//#define ODD 1
//int main() {
//	int i = 3;
//	switch (i & 1) {
//	case EVEN:cout << "even";
//		break;
//	case ODD: cout << "odd";
//		break;
//	default:cout << "default";
//	}
//	return 0;
//}
#include <iostream>
using namespace std;


int main() {
	int Array1[] = { 1, 2, 3, 5, 8, 13, 21, 34, 55, 89 };
	int Array2[] = { 2, 3, 5, 7, 11, 13, 17, 19, 23, 29 };
	int common[100];
	int i, j;
	int n = 0;
	for (i = 0; i < 10; ++i) {
		for (j = 0; j < 10; ++j) {
			if (Array1[i] == Array2[j]) {
				common[j] = Array2[j];
				++n;
			}
		}
	}
	printf("The totla number of common elements is %d\n", n);
	return 0;
}
