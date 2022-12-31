#include "graphs.hpp"



//nodes are represented numbers from 0 to NODES (excluded)
int NODES;
int EDGES_N;
vector<pair<int,int>> EDGES[NODES_MAX];



int main() {
	srand(time(NULL));
	double timer;

	random_graph(NODES, EDGES_N, EDGES);
	cout << NODES << "\n\n";

	//print_graph(EDGES, NODES);

	//FloydWarshall(NODES, EDGES);
	//print_FloydWarshall(NODES);
	
	timerStart(timer);
	FloydWarshall(NODES, EDGES);
	cout << "Floyd-Warshall (check):\t\t\t" << negativeCycles_FloydWarshall(NODES) << ": " << timerEnd(timer) << "\n\n";

	timerStart(timer);
	cout << "negative cycles(Floyd-Warshall):\t" << check_FloydWarshall(NODES, EDGES) << ": " << timerEnd(timer) << "\n\n";

	timerStart(timer);
	cout << "negative cycles(Bellman-Ford):\t\t" << negativeCycles_BellmanFord(NODES, EDGES) << ": " << timerEnd(timer) << endl;
}