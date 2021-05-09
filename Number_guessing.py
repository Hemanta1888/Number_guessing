import random
Number_to_guess = random.randint(1 , 25)

while True:
    name=input("Enter your name: ")
    print(f"Hello, {name}!")

    question = input('would you like to play one game with me? [y/n] ')

    if question == "n":
        print("okay, No problem")
        print("Bye........")
        break
        
    if question == "y":
        print("Thank you for agree with me to play the game.")
        print("I'm thinking a number between 1 and 25. So, you have to guess the number")


    Number_of_tries = 0

    while Number_to_guess != "guess":

        if Number_of_tries == 4:
            print(f"sorry {name},you lost the game!")
            print(f"The Number was {Number_to_guess}.")
            break
        guess = int(input("Please guess a number between 1 and 25: "))
        if guess < Number_to_guess:
            print("your guess is smaller than the number")
        elif guess > Number_to_guess:
            print("your guess is higher than the number")
        else:
            print(f"Well done {name}, you won! The number was {Number_to_guess}. It tooks only {Number_of_tries} number of tries.")
            break
        Number_of_tries += 1
