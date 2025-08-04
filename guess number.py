number = 86
for x in range(0,10):
    guess = int(input("guess the number: "))    
    if guess > number:
        print("choose a smaller number ")
    elif guess < number:
        print("choose a bigger number ")
    else:
        print("you found it!!!") 
        break      