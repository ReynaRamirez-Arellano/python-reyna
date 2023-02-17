import random

def game():
    # Generate a random number
    number = str(random.randint(100, 999))
    print("Welcome to the Number Baseball Game!")
    print("Guess a 3-digit number:")

    # Start the game
    for i in range(10):
        guess = input()
        if guess == number:
            print("Congratulations! You won in", i+1, "tries!")
            return
        else:
            strike, ball = 0, 0
            for j in range(3):
                if guess[j] in number:
                    if guess[j] == number[j]:
                        strike += 1
                    else:
                        ball += 1
            print(strike, "strikes,", ball, "balls.")
    print("Sorry, you lost. The number was", number + ".")

if __name__ == "__main__":
    game()
