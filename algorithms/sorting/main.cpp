#include "sorting.hpp"


int A[N];




int main() {
	srand(time(NULL));
	double timer;

	randomArray(A, N, RANGE);


////SORT
	timerStart(timer);
	quickSort(A, 0, N);
	cout << "QuickSort: " << timerEnd(timer) << endl;
	//printArray(A, 0, N);
	cout << checkAscending(A, 0, N) << endl;
	cout << endl;

	randomArray(A, N, RANGE);
	timerStart(timer);
	random_quickSort(A, 0, N);
	cout << "random_QuickSort: " << timerEnd(timer) << endl;
	//printArray(A, 0, N);
	cout << checkAscending(A, 0, N) << endl;
	cout << endl;

	randomArray(A, N, RANGE);
	timerStart(timer);
	radixSort(A, N);
	cout << "RadixSort: " << timerEnd(timer) << endl;
	//printArray(A, 0, N);
	cout << checkAscending(A, 0, N) << endl;
	cout << endl;

////SELECT
	int k = rand() % N + 1;
	randomArray(A, N, RANGE);
	//printArray(A, 0, N);
	timerStart(timer);
	cout << quickSelect(A, 0, N, k) << endl;
	cout << "QuickSelect " << k << ": " << timerEnd(timer) << endl;

	randomArray(A, N, RANGE);
	//printArray(A, 0, N);
	timerStart(timer);
	cout << random_quickSelect(A, 0, N, k) << endl;
	cout << "random_QuickSelect " << k << ": " << timerEnd(timer) << endl;

	randomArray(A, N, RANGE);
	//printArray(A, 0, N);
	timerStart(timer);
	cout << medianSelect(A, 0, N, k) << endl;
	cout << "MedianSelect " << k << ": " << timerEnd(timer) << endl;

	randomArray(A, N, RANGE);
	//printArray(A, 0, N);
	timerStart(timer);
	cout << A[bubbleSelect(A, 0, N, k)] << endl;
	cout << "BubbleSelect " << k << ": " << timerEnd(timer) << endl;


}