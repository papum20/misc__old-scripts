#include "sorting.hpp"


intQueue newIntQueue() {
	intQueue q = new intDeQue;
	q->front = q->back = NULL;
	return q;
}
bool emptyInt(intQueue q) {
	return q->front == NULL;
}
int frontInt(intQueue q) {
		return q->front->val;
	}
void pushInt(intQueue q, int e) {
		intList tmp = new intPointer;
		tmp->val = e;
		tmp->next = NULL;
		if(q->back == NULL) q->back = q->front = tmp;
		else {
			q->back->next = tmp;
			q->back = tmp;
		}
	}
void popInt(intQueue q) {
		if(q->front != NULL) {
			intList tmp = q->front;
			q->front = tmp->next;
			if(q->front == NULL) q->back = NULL;
			delete tmp;
		}
	}




/*
void radixSort(int V[], int n) {
		int max_digits = log(INT32_MAX) / log(DIGITS_BASE);
		for(int d = 0; d <= max_digits; d++) {
			for(int i = 0; i < n; i++) {
				int current_digit = (int)(V[i] / pow(DIGITS_BASE, d)) % DIGITS_BASE;
				buckets[current_digit].push(V[i]);
			}
			int ind = 0;
			for(int i = 0; i < DIGITS_BASE; i++) {
				while(!buckets[i].empty()) {
					V[ind++] = buckets[i].front();
					buckets[i].pop();
				}
			}
		}
	}
*/

/*
void radixSort(int V[], int n) {
		for(int i = 0; i < DIGITS_BASE; i++) buckets[i] = newIntQueue();
		int max_digits = log(INT32_MAX) / log(DIGITS_BASE);
		for(int d = 0; d <= max_digits; d++) {
			for(int i = 0; i < N; i++) {
				int current_digit = (int)(V[i] / pow(DIGITS_BASE, d)) % DIGITS_BASE;
				pushInt(buckets[current_digit], V[i]);
			}
			int ind = 0;
			for(int i = 0; i < DIGITS_BASE; i++) {
				while(!emptyInt(buckets[i])) {
					V[ind++] = frontInt(buckets[i]);
					popInt(buckets[i]);
				}
			}
		}
	}
*/


void radixSort(int V[], int n) {
		for(int i = 0; i < DIGITS_BASE; i++) bucket_sizes[i] = 0;
		int max_digits = log(INT32_MAX) / log(DIGITS_BASE);
		for(int d = 0; d <= max_digits; d++) {
			for(int i = 0; i < n; i++) {
				int current_digit = (int)(V[i] / pow(DIGITS_BASE, d)) % DIGITS_BASE;
				buckets[current_digit][bucket_sizes[current_digit]++] = V[i];
			}
			int ind = n - 1;
			for(int i = DIGITS_BASE - 1; i >= 0; i--)
				while(bucket_sizes[i] > 0) V[ind--] = buckets[i][--bucket_sizes[i]];
		}
	}
