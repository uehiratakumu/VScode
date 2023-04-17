#include<iostream>
#include<iomanip>
#include<cmath>

double f(double x) {
	return exp(x) + x * x - 2;
}

double g(double x) {
	return exp(x) + 2 * x;
}

double Newton(double x) {
	const double eps = 1e-08;

	while (fabs(f(x) > eps)) {
		x = x - f(x) / g(x);
	}
	return x;
}

int main() {

	double x;
	std::cin >> x;
	std::cout << std::setprecision(6) << std::fixed << (double)Newton(x) << std::endl;
	return 0;
}