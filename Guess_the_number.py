import random
while True:
    target =random.randint(1,100)
    print("\nA new game has started! Guess the number between 1 and 100")
    while True:
        choice = input("Guess a number or Quit: ").strip().lower()
        if choice == "quit":
            print("Thank you for playing!")
            print("---GAME OVER---")
            exit()
        if choice.isdigit():
            guess = int(choice)
            if guess == target:
                print("Congratulations! You have guessed the number!")
                break
            elif guess < target:
                print("Your number is less than the Target number")
            else:
                print("Your number is greater than the Target number") 
        else:
            print("Please enter a valid number or quit")        

               
