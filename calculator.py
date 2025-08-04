num_1 = int(input("enter 1st number: "))
num_2 = int(input("enter 2nd number: "))
amalgar = input("equation?(+ - * /): ")
if amalgar == "+" :
    print("the answer is: ", (num_1 + num_2))
elif amalgar == "-" :
    print("the answer is: ", (num_1 - num_2))
elif amalgar == "*" :
    print("the answer is: ", (num_1 * num_2))
else :
    print("the answer is: ", (num_1 / num_2))