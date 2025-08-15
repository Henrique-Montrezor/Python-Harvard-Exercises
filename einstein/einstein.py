def main():
    mass_kg = int(input("m: "))

    speed_of_light = 300000000

    energy_joules = mass_kg * (speed_of_light ** 2)

    print(f"E: {energy_joules}")


main()
