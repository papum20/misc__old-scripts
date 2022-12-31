main: help.o main.o quickselect.o quicksort.o radixsort.o
	g++ help.o main.o quickselect.o quicksort.o radixsort.o -lncurses -o main

help.o: help.cpp
	g++ -c help.cpp
main.o: main.cpp
	g++ -c main.cpp
quickselect.o: quickselect.cpp
	g++ -c quickselect.cpp
quicksort.o: quicksort.cpp
	g++ -c quicksort.cpp
radixsort.o: radixsort.cpp
	g++ -c radixsort.cpp



clean:
	rm *.o */*.o main main.exe