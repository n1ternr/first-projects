def fibonachi(n):
    a ,b = 0,1
    for x in range(n):
        print(a, end=" ")
        a,b = b, a+b
fibonachi(int(input("how many numbers should be printed? ")))        