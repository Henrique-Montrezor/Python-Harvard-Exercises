import inflect

def main():
    """
    Solicita nomes e os imprime em uma despedida formatada.
    """
    p = inflect.engine()
    names = []

    while True:
        try:
            name = input("Name: ")
            names.append(name)
        except EOFError:
            print()
            break

    if names:
        farewell_message = p.join(names)
        print(f"Adieu, adieu, to {farewell_message}")

if __name__ == "__main__":
    main()
