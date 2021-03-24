#include <iostream>
using namespace std;

int main()
{
	int n, a, x;
	cin >> n;
	x = n;
	a = 0;
	while(n > 1)
	{
		if ((n % 2) == 1)
		{
			n = 3 * n + 1;
			a++;
		}
		else
		{
			n = n / 2;
			a++;
		}
	}
	cout << "height : " << a<< "\n";
	cout << x << " is hailstone";
}