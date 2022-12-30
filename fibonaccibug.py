#!/usr/bin/env pypy3
# COMPLEXITY: O(KlogK) where the overall K is the sum of all K in an input
# IDEA: Since the fibonacci sequence grows exponentially, there are only log(K) possible degrees.
# Thus after filtering multiple offers for the same degree, we have log(K) offers.
# Then you can efficiently solve a knapsack problem for each day.


# input data
T = int(input().strip())
for _ in range(T):
    N, K = map(int, input().strip().split())
    A = [None] * N
    B = [None] * N
    for i in range(N):
        A[i], B[i] = map(int, input().strip().split())

    fibb = [1, 1]
    while fibb[-1] < K:
        fibb.append(fibb[-1] + fibb[-2])

    C = len(fibb)
    cost = [0] * C
    for i in range(N):
        if A[i] < C and B[i] > cost[A[i]]:
            cost[A[i]] = B[i]

    DP = [0] * (K+1)
    for i in range(C):
        for j in range(fibb[i], K+1):
            DP[j] = max(DP[j], DP[j-fibb[i]] + cost[i])

    print(DP[K])  # print the result
