import random


def main():

    level = get_level()
    score = 0

    for _ in range(10):
        errors = 0

        num_x = generate_integer(level)
        num_y = generate_integer(level)
        result = num_x + num_y

        while errors < 3:
            try:
                resposta = int(input(f"{num_x} + {num_y} = "))
                if resposta == result:
                    score += 1
                    break
                else:
                    errors +=1
                    print("EEE")

            except ValueError:
                errors += 1
                print("EEE")

            if errors == 3:
                print(f"{num_x} + {num_y} = {result}")


    print(f"Score: {score}")

def get_level():
    while True:
        try:
            level = int(input("Level: "))

            if level in [1,2,3]:
                return level

        except ValueError:
            pass

def generate_integer(level):

    if level == 1:
        return random.randint(0,9)
    elif level == 2:
        return random.randint(10,99)
    elif level == 3:
        return random.randint(100,999)

if __name__ == "__main__":
    main()
