def main():

    debit = 50

    while debit > 0:
        print(f"Amount Due: {debit}")

        insert_coin = int(input("Insira sua Moeda: "))

        if insert_coin in [5, 10, 25]:
            debit -= insert_coin

    change = abs(debit)

    print(f"Change Owed: {change}")

main()
