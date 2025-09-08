import re
import sys

def main():
    # Pede ao usuário um endereço IPv4 e o passa para a função de validação.
    print(validate(input("IPv4 Address: ")))

def validate(ip):
    """
    Validates an IPv4 address using regular expressions.
    Returns True if the format is valid, False otherwise.
    """
    # The regular expression below checks for the format X.X.X.X
    # Where each X is a number between 0 and 255.
    # r"..." -> indicates a raw string, so Python doesn't interpret backslashes.
    # ^ -> matches the beginning of the string.
    # (...) -> defines a group.
    # \. -> matches a literal period.
    # {3} -> indicates that the previous group and the period must repeat 3 times.
    # $ -> matches the end of the string.
    if matches := re.search(r"^([0-9]+)\.([0-9]+)\.([0-9]+)\.([0-9]+)$", ip):
        # If the overall format (numbers separated by periods) is correct,
        # now we check if each number is in the range 0 to 255.
        # matches.group(i) captures each of the four numbers.
        for i in range(1, 5):
            if int(matches.group(i)) > 255:
                return False
        return True 
    else:
        return False

if __name__ == "__main__":
    main()
