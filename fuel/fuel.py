def main():
    percentage = get_fuel_percentage()

    if percentage <= 1:
        print("E")
    elif percentage >= 99:
        print("F")
    else:
        print(f"{percentage}%")


def get_fuel_percentage():
    while True:
        fraction = input("Fraction: ")
        try:
            x_str, y_str = fraction.split('/')
            x = int(x_str)
            y = int(y_str)

            if not 0 <= x <= y:
                continue

            if y == 0:
                continue

            percentage = round((x / y) * 100)
            return percentage

        except (ValueError, ZeroDivisionError):
            pass


if __name__ == "__main__":
    main()

