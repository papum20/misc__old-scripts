#include "graphs.hpp"



int CACHE[NODES_MAX][NODES_MAX];




void FloydWarshall(int N, adjacents E[]) {
		//init cache with k=0
		for(int u = 0; u < N; u++) {
			for(int v = 0; v < N; v++) {
				if(u == v) CACHE[u][v] = 0;
				else CACHE[u][v] = find_weight(E, u, v);
			}
		}
		//print_FloydWarshall(N);
		//calculate paths
		for(int k = 0; k < N; k++) {
			for(int u = 0; u < N; u++) {
				for(int v = 0; v < N; v++) {
					if(CACHE[u][k] != INFINITE && CACHE[k][v] != INFINITE)
						CACHE[u][v] = min(CACHE[u][v], CACHE[u][k] + CACHE[k][v]);
				}
			}
			//print_FloydWarshall(N);
		}
	}

bool check_FloydWarshall(int N, adjacents E[]) {
		//init cache with k=0
		for(int u = 0; u < N; u++) {
			for(int v = 0; v < N; v++) {
				if(u == v) CACHE[u][v] = 0;
				else CACHE[u][v] = find_weight(E, u, v);
			}
		}
		//print_FloydWarshall(N);
		//calculate paths
		for(int k = 0; k < N; k++) {
			for(int u = 0; u < N; u++) {
				for(int v = 0; v < N; v++) {
					if(CACHE[u][k] != INFINITE && CACHE[k][v] != INFINITE)
						CACHE[u][v] = min(CACHE[u][v], CACHE[u][k] + CACHE[k][v]);
				}
			}
			if(negativeCycles_FloydWarshall(N)) return true;
			//print_FloydWarshall(N);
		}
		return false;
	}


void print_FloydWarshall(int N) {
		printf("\t");
		for(int v = 0; v < N; v++) printf("%d\t", v);
		cout << endl;
		for(int u = 0; u < N; u++) {
			printf("%d:\t", u);
			for(int v = 0; v < N; v++) {
				if(CACHE[u][v] == INFINITE) printf("/\t");
				else printf("%d\t", CACHE[u][v]);
			}
			cout << endl;
		}
		cout << endl;
	}

bool negativeCycles_FloydWarshall(int N) {
		for(int u = 0; u < N; u++)
			if(CACHE[u][u] < 0) return true;
		return false;
	}