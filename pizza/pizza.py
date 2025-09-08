import sys
from tabulate import tabulate
import csv

def main():
    try:
        if len(sys.argv) < 2:
            sys.exit('To few Command-line arguments')
        if len(sys.argv) > 2:
            sys.exit('To many Command-line arguments')
        if sys.argv[1].endswith('.csv') == False:
            sys.exit('Not a CSV file')
    except FileNotFoundError:
        sys.exit('This file does not exist')

    data_table = []
    with open(sys.argv[1]) as csvfile:

        reader = csv.reader(csvfile)
        cabecalho = next(reader)

        for row in reader:
            data_table.append(row)

        print(tabulate(data_table, headers=cabecalho, tablefmt="grid"))

main()

