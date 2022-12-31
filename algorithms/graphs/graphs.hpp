#ifndef GRAPHS_HPP
#define GRAPHS_HPP



#include <iostream>
#include <ctime>
#include <vector>
#include <algorithm>
using namespace std;



#define NODES_MIN 300
#define NODES_MAX 300
#define WEIGHT_MIN -10000
#define WEIGHT_MAX 50000
const int INFINITE = numeric_limits<int>::max();
#define NO_MARK -1
#define NO_ITERATION -1


typedef vector<pair<int,int>> adjacents;


////TEST/HELP
	//adjacents random_graph(int &N, int &M);
	void random_graph(int &N, int &M, vector<pair<int,int>> E[]);
	void print_graph(adjacents A[], int N);
	int find_weight(adjacents E[], int u, int v);			//returns infinite if cant find

	void timerStart(double &timer);
	double timerEnd(double &timer);

////FLOYD-WARSHALL
	void FloydWarshall(int N, adjacents E[]);
	bool check_FloydWarshall(int N, adjacents E[]);
	void print_FloydWarshall(int N);
	bool negativeCycles_FloydWarshall(int N);

////BELLMAN-FORD
	bool negativeCycles_BellmanFord(int N, adjacents E[]);		//bool if there are any negative cycles
	void BellmanFord(adjacents E[], int s);						//calculates min distances from source s
	bool check_BellmanFord(adjacents E[], int s);					//checks negative cycles in connected nodes
	bool recursiveVisit(adjacents E[], int u, int s);				//visit for bellman ford, returns bool if relaxed




#endif