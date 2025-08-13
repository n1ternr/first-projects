import random
def gol_ya_pooch():
    hands = ["left" , "right"]
    print("welcome to gol ya pooch player.")
    print("type 'quit' if you want to exit the game. ")
    while True:
        try:
            rounds = int(input("select how many times do you like to play? "))
        except ValueError:
            print("please enter a valid number: ")
            continue
        score = 0
        round_num = 1
        while round_num <= rounds:
            print(f"\n round {round_num} of {rounds}")    
            gol_hand = random.choice(hands)
            guess = input("which one? (Left/Right) ").lower()
            if guess == "quit":
                print("quiting game... ")
                break
            if guess not in hands:
                print("please enter: 'left' or 'right' ")
                continue
            if guess == gol_hand:
                print("you found it! :) ")
                print("gained a score!")
                score += 1
            else:
                print("wrong answer , :(")
            round_num += 1    
        score_percent = (score / rounds) * 100
        print(f"\n your score is {score} point(s) out of {rounds} rounds")
        print("your winning percentage is:" , int(score_percent) , "% ")           
        restart_game = input("restart? (Y/N) ").lower()
        if restart_game != "y":
            print("thanks for playing :) ")
            break    
gol_ya_pooch()    