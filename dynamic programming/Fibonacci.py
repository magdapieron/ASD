def fib(n):
    if n < 2:
        return 1
    return fib(n-1) + fib(n-2)

def fib_dynamic1(n):
    fib = [1]*(n+1)
    for i in range(2,n+1):
        fib[i] = fib[i-1] + fib[i-2]
    return fib[n]

def fib_dynamic2(n):
    f1 = f2 = 1     # f1 poprzedni, f2 dwa wcześniej
    if n < 2:
        return f1
    for i in range(3,n+1):
        f = f1+f2
        f2 = f1
        f1 = f
    return f
