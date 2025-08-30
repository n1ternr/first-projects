def sum(n):
    a,b = 1,2
    print(a)
    for x in range(n-1):
        current = a + b
        print(current)
        a,b = b ,  current
sum(int(input("how many times should i calculate? ")))
        