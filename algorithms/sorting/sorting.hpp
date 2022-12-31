#ifndef SORTING_HPP
#define SORTING_HPP


#include <iostream>
#include <ctime>
#include <cmath>
#include <queue>
using namespace std;


#define N 10000000
#define RANGE 1000000000


//RADIXSORT
#define DIGITS_BASE 4



struct intPointer {
	int val;
	intPointer *next;
};
typedef intPointer *intList;
struct intDeQue {
	intList front;		//pop
	intList back;		//push
};
typedef intDeQue *intQueue;

intQueue newIntQueue();
bool emptyInt(intQueue q);
int frontInt(intQueue q);
void pushInt(intQueue q, int e);
void popInt(intQueue q);


//queue<int> buckets[DIGITS_BASE];
//intQueue buckets[DIGITS_BASE];
int buckets[DIGITS_BASE][N];
int bucket_sizes[DIGITS_BASE];






////HELP
	void swap(int V[], int x, int y);

////SORTING
	//QUICKSORT
	int partition(int V[], int a, int b, int pivot);	//a included, b excluded
	int firstPartition(int V[], int a, int b);			//a included, b excluded
	int randomPartition(int V[], int a, int b);			//a included, b excluded

	int firstPivot(int a, int b);						//a included, b excluded
	int randomPivot(int a, int b);						//a included, b excluded

	void quickSort(int V[], int a, int b);				//a included, b excluded
	void random_quickSort(int V[], int a, int b);		//a included, b excluded

	//RADIXSORT
	void radixSort(int V[], int n);

////SELECTION
	void flagPartition(int V[], int a, int b, int pivot_i, int &pivot1, int &pivot2);
	int quickSelect(int V[], int a, int b, int k);
	int random_quickSelect(int V[], int a, int b, int k);

	int bubbleSelect(int V[], int a, int b, int k);		//returns median index
	int medianSelect(int V[], int a, int b, int k);


////TEST
	void randomArray(int V[], int n, int range);
	void printArray(int V[], int a, int b);				//a included, b excluded

	bool checkAscending(int V[], int a, int b);			//a included, b excluded

	void timerStart(double &timer);
	double timerEnd(double &timer);



#endif