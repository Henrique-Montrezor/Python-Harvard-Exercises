def main():

    camel_case_input = input("camelCase:")

    print("snake_case: ", end="")

    for frase in camel_case_input:
        if frase.isupper():
            print("_", end="")

        print(frase.lower(), end="")

    print()

main()
