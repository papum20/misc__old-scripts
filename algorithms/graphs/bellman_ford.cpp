#include "graphs.hpp"




int MARKS[NODES_MAX];				//marks for nodes
int USED[NODES_MAX][NODES_MAX];		//for recursion: number of iteration
int D[NODES_MAX];					//min distances
int CONNECTED[NODES_MAX];

int iteration, connected_nodes;



bool negativeCycles_BellmanFord(int N, adjacents E[]) {
		for(int i = 0; i < N; i++) {
			D[i] = INFINITE;
			MARKS[i] = NO_MARK;
			for(int j = 0; j < N; j++) USED[i][j] = NO_ITERATION;
		}
		int source = 0;

		while(source < N) {
			MARKS[source] = source;
			D[source] = 0;
			//cout << source << "::" << endl;

			BellmanFord(E, source);
			if(check_BellmanFord(E, source)) return true;
			else
				while(source < N && MARKS[source] != NO_MARK) source++;		
		}
		return false;
	}



void BellmanFord(adjacents E[], int s) {
		iteration = 0, connected_nodes = 1;
		CONNECTED[0] = s;
		while(iteration < connected_nodes && recursiveVisit(E, s, s)) {
			iteration++;
		}
	}

bool recursiveVisit(adjacents E[], int u, int s) {
		bool relaxed = false;
		for(int i = 0; i < connected_nodes; i++) {
			u = CONNECTED[i];
			for(auto v:E[u]) {
				if(MARKS[v.first] == NO_MARK) {
					MARKS[v.first] = s;
					CONNECTED[connected_nodes++] = v.first;
					D[v.first] = D[u] + v.second;
					relaxed = true;
				}
				else if(MARKS[v.first] == s && D[u] + v.second < D[v.first]) {
					D[v.first] = D[u] + v.second;
					relaxed = true;
				}
			}
		}
		return relaxed;
	}

bool check_BellmanFord(adjacents E[], int s) {
		return recursiveVisit(E, s, s);
	}

/*
void BellmanFord(adjacents E, int s) {
		iteration = 0, connected_nodes = 1;
		while(iteration < connected_nodes && recursiveVisit(E, s, s)) {
			iteration++;
			/*for(int i = 0; i < 5; i++) cout << MARKS[i] << " ";
			cout << endl;
			for(int i = 0; i < 5; i++) cout << USED[i] << " ";
			cout << endl;
			for(int i = 0; i < 5; i++) cout << D[i] << " ";
			cout << endl;
			cout << iteration << " " << connected_nodes << endl;*
		}
	}


bool check_BellmanFord(adjacents E, int s) {
		iteration++;
		return recursiveVisit(E, s, s);
	}


bool recursiveVisit(adjacents E, int u, int s) {
		bool relaxed = false;
		for(int i = 0; i < E[u].size(); i++) {
			pair<int, int> v = E[u][i];
			if(MARKS[v.first] == NO_MARK) {
				relaxed = true;
				MARKS[v.first] = s;
				connected_nodes++;
				USED[u][i] = iteration;
				D[v.first] = D[u] + v.second;
				recursiveVisit(E, v.first, s);
			}
			else if(MARKS[v.first] == s && USED[u][i] < iteration) {
				if(D[u] + v.second < D[v.first]) {
					relaxed = true;
					D[v.first] = D[u] + v.second;
				}
				USED[u][i] = iteration;
				if(recursiveVisit(E, v.first, s)) relaxed = true;
			}
		}
		return relaxed;
	}
	*/