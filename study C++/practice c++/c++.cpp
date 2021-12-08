#include <iostream>
using namespace std;

struct Player {
	char name[20];
	int intial_soldiers;
};
int main() {
	int n, s1, s2, f1, f2;
	cin >> n;
	Player P1, P2;
	cin >> P1.name >> f1;
	cin >> P2.name >> f2;
	P1.intial_soldiers = f1;
	P2.intial_soldiers = f2;
	for (int i = 0; i < n; i++) {
		cin >> s1 >> s2;
		if (s1 > s2)
			s1 /= 2;
		else if (s1 == s2) {
			s1 /= 2;
			s2 /= 2;
		}
		else
			s2 /= 2;
		P1.intial_soldiers -= s1;
		P2.intial_soldiers -= s2;
		if (P1.intial_soldiers <= 0 || P2.intial_soldiers <= 0)
			break;
	}
	if (P1.intial_soldiers < P2.intial_soldiers)
		cout << P2.name;
	else if (P1.intial_soldiers > P2.intial_soldiers)
		cout << P1.name;
	else {
		if (f1 < f2)
			cout << P2.name;
		else
			cout << P1.name;
	}
	cout << P1.intial_soldiers << " " << P2.intial_soldiers;
	return 0;
}