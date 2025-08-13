/**
 * Ejercicio B. SumaDosGrandes
 */

// #include <bits/stdc++.h>
#include <iostream>
using namespace std;

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(0);

	int max1, max2;

	for (int i = 0; i < 6; i++) {
		int numero;
		cin >> numero;

		if (i == 0) {
			max1 = numero;
		}
		else if (i == 1) {
			if (numero > max1) {
                max2 = max1;
                max1 = numero;
            }
			else {
                max2 = numero;
            }
        }
		else {
			if (numero > max1) {
                max2 = max1;
                max1 = numero;
            }
			else if (numero > max2) {
                max2 = numero;
            }
        }
	}

	cout << max1 + max2;

	return 0;
}
