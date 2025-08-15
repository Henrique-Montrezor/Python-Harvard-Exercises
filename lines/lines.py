import sys

def main():
    try:
        if len(sys.argv) < 2:
            sys.exit("Too few Command-lines arguments")

        elif len(sys.argv) > 2:
            sys.exit("Too many Command-lines arguments")

        elif sys.argv[1].endswith(".py") == False:
            sys.exit("Not a Python file")
            
    except FileNotFoundError:
        sys.exit("File does not exist")

    read_lines(sys.argv[1])


def read_lines(path):
    numbers = 0

    with open(path) as file:

        for lines in file:
            clean_lines = lines.strip()
            if clean_lines.startswith('#') or clean_lines == '':
                continue
            numbers = numbers + 1

    print(numbers)

main()


