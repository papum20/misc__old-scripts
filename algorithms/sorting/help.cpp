#include "sorting.hpp"





void swap(int V[], int x, int y) {
		int tmp = V[x];
		V[x] = V[y];
		V[y] = tmp;
	}



void randomArray(int V[], int n, int range) {
		for(int i = 0; i < n; i++) V[i] = rand() % range;
	}

void printArray(int V[], int a, int b) {
		for(int i = a; i < b; i++) cout << V[i] << " ";
		cout << endl;
	}


/*bool checkAscending(int V[], int a, int b) {
	if(a % 50000 == 0)cout << a << endl;
		if(a + 1 >= b) return true;
		else if(V[a] <= V[a+1]) return checkAscending(V, a + 1, b);
		else return false;
	}*/
bool checkAscending(int V[], int a, int b) {
		for(int i = a; i + 1 < b; i++)
			if(V[i] > V[i+1]) return false;
		return true;
	}



void timerStart(double &timer) {
		timer = clock();
	}
double timerEnd(double &timer) {
		timer = (clock() - timer) / CLOCKS_PER_SEC;
		return timer;
	}