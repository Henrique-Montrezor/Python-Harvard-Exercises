import csv
import sys

def main():

    if len(sys.argv) < 3:
        sys.exit("Too few Command-line Argument")

    elif len(sys.argv) > 3:
        sys.exit("Too many Command-line Argument")

    file_path = sys.argv[1]
    file_path_2 = sys.argv[2]


    try:
        with open(file_path) as file_input, open(file_path_2, 'w', newline='') as file_output:
            reader = csv.reader(file_input)
            writer = csv.writer(file_output)

            next(reader)

            writer.writerow(["first", "last", "house"])


            for row in reader:
                last_name,first_name = row[0].split(',')
                house = row[1]

                nova_linha = [first_name.strip(), last_name.strip(), house]
                writer.writerow(nova_linha)


    except FileNotFoundError:
        sys.exit("This file does not exist")



main()
