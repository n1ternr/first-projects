string = input("give me a word: ")
removal = int(input("how many letters should i remove? "))
if removal < len(string):
        result = string[removal: ]
        print(f"result: {result}")
else:
        print("too many chars to remove! ")