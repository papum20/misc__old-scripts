main: bellman_ford.o floyd_warshall.o help.o main.o
	g++ bellman_ford.o floyd_warshall.o help.o main.o -lncurses -o main

bellman_ford.o: bellman_ford.cpp
	g++ -c bellman_ford.cpp
floyd_warshall.o: floyd_warshall.cpp
	g++ -c floyd_warshall.cpp
help.o: help.cpp
	g++ -c help.cpp
main.o: main.cpp
	g++ -c main.cpp



clean:
	rm *.o */*.o main main.exe