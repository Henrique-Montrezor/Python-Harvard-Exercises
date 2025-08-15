import random
import sys

def main():
    level = get_level()
    secret_number = random.randint(1, level)

    while True:
        guess = get_guess()
        if guess < secret_number:
            print("Too small!")
        elif guess > secret_number:
            print("Too large!")
        else:
            print("Just right!")
            sys.exit()

def get_level():
    while True:
        try:
            n = int(input("Level: "))
            if n > 0:
                return n
        except ValueError:
            pass

def get_guess():
    while True:
        try:
            g = int(input("Guess: "))
            if g > 0:
                return g
        except ValueError:
            pass

if __name__ == "__main__":
    main()
