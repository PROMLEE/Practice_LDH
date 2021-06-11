#include <iostream>
using namespace std;

class Power {
	int kick;
	int punch;
public:
	Power(int kick = 0, int punch = 0) {
		this->kick = kick;
		this->punch = punch;
	}
	void show();
	friend Power operator+(Power op1, Power op2); // 프렌드 선언
};

void Power::show() {
	cout << "kick = " << kick << ", " << "punch = " << punch << endl;
}
Power operator+(Power op1, Power op2) {
	Power tmp;
	tmp.kick = op1.kick + op2.kick;
	tmp.punch = op1.punch + op2.punch;
	return tmp;
}



int main() {
	int i, j, p, q;
	cin >> i >> j >> p >> q;
	Power a(i, j), b(p, q), c;
	c = a + b; // 파워 객체 + 연산
	a.show();
	b.show();
	c.show();
}