def main():

    valor_devido = 50

    while valor_devido > 0:
        print(f"Amount Due: {valor_devido}")

        moeda_inserida = int(input("Insira sua Moeda: "))

        if moeda_inserida in [5, 10, 25]:
            valor_devido -= moeda_inserida

    troco_devido = abs(valor_devido)

    print(f"Change Owed: {troco_devido}")

main()
