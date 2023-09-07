#include <iostream>
#include <string.h>
#include <fstream>//ファイルのインプット、アウトプット fileIO
#include <vector>//STLのvectorクラス, 動的配列を操作するライブラリ
#include<cmath>
​
struct _data {
	double x;
	double y;
};
​
std::vector<_data> data;
​
void read() {
	int N;
	std::cin >> N;
	double x, y;
	for (int i = 0; i < N; i++) {//ファイルの最終行まで読む
		std::cin >> x >> y;
		_data tmp;
		tmp.x = x;
		tmp.y = y;
​
		data.push_back(tmp);
	}
}
​
//最小二乗法でフィットする関数の定義
double f0(double x) {
	return 1.;//定数項
}
​
double f1(double x) {
	return x;
}
​
double f2(double x) {
	return x * x;
}
​
double f3(double x) {
	return pow(x, 3);
}
​
double f4(double x) {
	return pow(x, 4);
}
double f5(double x) {
	return pow(x, 5);
}
​
int main() {
	(void)read();
	const int row_num = (int)data.size();// the number of rows データ数 (x,y)の数
	const int col_num = 6;// the number of columns モデル変数の数
​
	//coefficient matrix G declaration
	double** G;
	G = new double* [row_num];
	for (int i = 0; i < row_num; i++) {
		G[i] = new double[col_num] {};
	}
​
	// Z declaration
	double* Z;// [row_num] ;
	Z = new double[row_num];
​
	// G.Z 
	double (*funcp[])(double) = { f0,f1,f2, f3, f4, f5 };//関数ポインタ
	for (int i = 0; i < row_num; i++) {
		double x = data[i].x;
		double y = data[i].y;
​
		for (int j = 0; j < col_num; j++) {
			G[i][j] = funcp[j](x);
		}
​
		Z[i] = y;
	}
​
	//A = GT * G
	double A[col_num][col_num];
	memset(A, 0, sizeof(double) * col_num * col_num);//all components are set to zero
	for (int i = 0; i < col_num; i++) {
		for (int j = 0; j < col_num; j++) {
			double aij = 0.;
			for (int k = 0; k < row_num; k++) {
				aij += G[k][i] * G[k][j];// GT[i][k]*G[k][j] = G[k][i]*G[k][j]
			}
			A[i][j] = aij;
		}
	}
​
	//B = GT * Z
	double B[col_num];
	for (int i = 0; i < col_num; i++) {
		double bi = 0.;
		for (int k = 0; k < row_num; k++) {
			bi += G[k][i] * Z[k];// GT[i][k] * Z[k] = G[k][i] * Z[k]
		}
		B[i] = bi;
	}
​
	// L declaration
	double L[col_num][col_num];//row 3, column 3
	memset(L, 0, sizeof(double) * col_num * col_num);//all components are set to zero
​
	// L . A -> U
	for (int i = 0; i < col_num; i++) {
		double aii = A[i][i];
​
		for (int j = i; j < col_num; j++) {
			L[j][i] = A[j][i];
		}
​
		for (int j = 0; j < col_num; j++) {
			A[i][j] /= aii; //for i-th row // <-- A[i][j] = A[i][j] / aii;
		}
​
		for (int j = i + 1; j < col_num; j++) {
			double aji = A[j][i];
			for (int l = i; l < col_num; l++) {
				A[j][l] -= aji * A[i][l];// <-- A[j][l] = A[j][l] - aji * A[i][l];
			}
		}
	}
​
	// Y = U * a
	double Y[col_num];
	// forward substitution
	for (int i = 0; i < col_num; i++) {
		double tmp = 0.0;
		for (int j = 0; j < i; j++) {
			tmp += L[i][j] * Y[j];
		}
		Y[i] = B[i] - tmp;
		Y[i] /= L[i][i];
	}
​
​
	// X = [a0, a1, a2, ...]
	double X[col_num]{};
	// backward substitution
	for (int i = (col_num - 1); i >= 0; i--) {
		double tmp = 0.0;
		for (int j = (i + 1); j < col_num; j++) {
			tmp += A[i][j] * X[j];
		}
		X[i] = Y[i] - tmp;
	}
​
	//output
	for (int i = 0; i < col_num; i++) {
		printf("%.6f\n", X[i]);
	}
}
​