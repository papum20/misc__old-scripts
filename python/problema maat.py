def f(n, time):
    if(time == 10):
        return n
    else:
        return f(n**2 * (3-2*n), time+1)




print(f(2020, 0))
