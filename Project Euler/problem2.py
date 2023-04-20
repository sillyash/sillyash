def fibo_dyn(n:int)->int:
    assert n >= 0
    T = [0]*(n+2)
    T[0] = 1
    T[1] = 2
    for i in range(2, n):
        T[i] = T[i-1] + T[i-2]
    return T[n-1]

def problem2(n:int)->int:
    s = 0
    a = 1
    x = 1
    while x <= n:
        if x%2 == 0:
            s += x
        x = fibo_dyn(a)
        a += 1
    return s

print(problem2(4000000))   
    
