#include "graphs.hpp"




/*
adjacents random_graph(int &N, int &M) {
		N = (rand() % (NODES_MAX - NODES_MIN + 1)) + NODES_MIN;
		adjacents A(N);
		int EDGES_MAX = N * (N - 1);
		M = rand() % EDGES_MAX;

		vector<pair<int, int>> ALL_EDGES(N*(N-1));
		int ind = 0;
		for(int u = 0; u < N; u++) {
			for(int v = 0; v < N; v++) {
				if(u != v) ALL_EDGES[ind++] = {u, v};
			}
		}

		for(int e = 0; e < M; e++) {
			int r = rand() % ALL_EDGES.size();
			int w = (rand() % (WEIGHT_MAX - WEIGHT_MIN + 1)) + WEIGHT_MIN;
			A[ALL_EDGES[r].first].push_back({ALL_EDGES[r].second, w});
			ALL_EDGES.erase(ALL_EDGES.begin() + r);
		}

		for(int i = 0; i < N; i++) sort(A[i].begin(), A[i].end());
		return A;
	}
*/

void random_graph(int &N, int &M, vector<pair<int,int>> E[]) {
		N = (rand() % (NODES_MAX - NODES_MIN + 1)) + NODES_MIN;
		int EDGES_MAX = N * (N - 1);
		M = rand() % EDGES_MAX;

		vector<pair<int, int>> ALL_EDGES(N*(N-1));
		int ind = 0;
		for(int u = 0; u < N; u++) {
			for(int v = 0; v < N; v++) {
				if(u != v) ALL_EDGES[ind++] = {u, v};
			}
		}

		for(int e = 0; e < M; e++) {
			int r = rand() % ALL_EDGES.size();
			int w = (rand() % (WEIGHT_MAX - WEIGHT_MIN + 1)) + WEIGHT_MIN;
			E[ALL_EDGES[r].first].push_back({ALL_EDGES[r].second, w});
			ALL_EDGES[r] = ALL_EDGES[--ind];
		}

		for(int i = 0; i < N; i++) sort(E[i].begin(), E[i].end());
	}


void print_graph(adjacents A[], int N){
		//edges
		printf("total size: %d.\n", N);
		for(int i = 0; i < N; i++) {
			printf("%d: size %d:\t", i, A[i].size());
			for(auto j:A[i]) cout << j.first << "\t";
			cout << endl;
		}
		cout << endl;
		//weights
		printf("total size: %d.\n", N);
		for(int i = 0; i < N; i++) {
			printf("%d: size %d:\t", i, A[i].size());
			for(auto j:A[i]) cout << j.second << "\t";
			cout << endl;
		}
		cout << endl;
	}


int find_weight(adjacents E[], int u, int v) {
		for(auto x:E[u])
			if(x.first == v) return x.second;
		return INFINITE;
	}




////TIMER

void timerStart(double &timer) {
		timer = clock();
	}
double timerEnd(double &timer) {
		timer = (clock() - timer) / CLOCKS_PER_SEC;
		return timer;
	}