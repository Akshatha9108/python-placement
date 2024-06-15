import random
def generate_random_number(low,high):
    return random.randint(low,high)
def check_guess(secret_number,guess):
    if guess<secret_number:
        return "Too Low"
    elif guess>secret_number:
        return "Too high"
    else:
        return "corret!"
def main():
    low=1
    high=100
    secret_number=generate_random_number(low,high)
    print("welcome to the Number guessinf Game!")
    print(f"Guess the number between {low} and {high}.")

    guess=0
    while True:
        guess=int(input("enter the guess:"))
        result=check_guess(secret_number,guess)
        print(result)
        guess+=1
        if result == "corret!":
            print(f"You guessed the number in {guess} guesses.")
            break
if __name__=="__main__":
    main()    