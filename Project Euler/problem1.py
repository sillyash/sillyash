def multiples(n1:int, n2:int, n:int)->list:
    li = [n1]
    for i in range(n1+1, n):
        if (i % n1 == 0) or (i % n2 == 0):
            li.append(i)
    return li


print(sum(multiples(3,5,1000)))
