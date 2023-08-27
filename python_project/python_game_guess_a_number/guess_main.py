import random

def guess_the_number():
    # Generate a random number between 1 and 10
    target_number = random.randint(1, 10)
    attempts = 0

    print("A number between 1 and 10. Do you know what is that?")

    while True:
        player_guess = int(input("Enter your guess: "))
        attempts += 1

        if player_guess < target_number:
            print("Too small")
        elif player_guess > target_number:
            print("Too big")
        else:
            print(f"Congratulations! You guessed the number {target_number} in {attempts} attempts.")
            break

if __name__ == "__main__":
   
   '''
    if __name__ == "__main__": block ensures that the game starts only when
    the script is run directly. If someone were to import your game module into another script, 
    they could use the functions or classes you defined without automatically starting the game.
   '''

   guess_the_number()
