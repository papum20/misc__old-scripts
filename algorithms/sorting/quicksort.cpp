#include "sorting.hpp"



int partition(int V[], int a, int b, int pivot) {
		swap(V, a, pivot);
		int s = a + 1, e = b - 1;
		while(s <= e) {
			while(s <= e && V[s] <= V[a]) s++;
			while(s <= e && V[e] > V[a]) e--;
			if(s < e) swap(V, s, e);
		}
		swap(V, a, e);
		return e;
	}
int firstPartition(int V[], int a, int b) {
		return partition(V, a, b, firstPivot(a, b));
	}
int randomPartition(int V[], int a, int b) {
		int pivot = randomPivot(a, b);
		//cout << pivot << endl;
		return partition(V, a, b, pivot);
	}



int firstPivot(int a, int b) {
		return a;
	}
int randomPivot(int a, int b) {
		return (rand() % (b - a) + a);
	}



void quickSort(int V[], int a, int b) {
	if(b - a > 1) {
		int pivot = firstPivot(a, b);
		int m = partition(V, a, b, pivot);
		quickSort(V, a, m);
		quickSort(V, m + 1, b);
	}
}
void random_quickSort(int V[], int a, int b) {
	if(b - a > 1) {
		int pivot = randomPivot(a, b);
		int m = partition(V, a, b, pivot);
		random_quickSort(V, a, m);
		random_quickSort(V, m + 1, b);
	}
}