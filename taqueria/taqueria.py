def main():
    """
    Simula o caixa de uma taqueria, somando os pedidos do usuário
    e exibindo o total a cada item.
    """
    menu = {
        "baja taco": 4.25,
        "burrito": 7.50,
        "bowl": 8.50,
        "nachos": 11.00,
        "quesadilla": 8.50,
        "super burrito": 8.50,
        "super quesadilla": 9.50,
        "taco": 3.00,
        "tortilla salad": 8.00
    }

    # Inicializa o custo total do pedido
    total_cost = 0.0

    # Loop infinito para receber os pedidos
    while True:
        try:
            # Pede ao usuário para digitar um item
            item = input("Item: ").lower()

            # Se o item estiver no menu, adiciona o preço ao total
            if item in menu:
                total_cost += menu[item]
                # Exibe o total formatado como moeda
                print(f"Total: ${total_cost:.2f}")

        except EOFError:
            # O usuário pressionou Ctrl+D para finalizar o pedido
            print() # Imprime uma nova linha para formatar a saída do terminal
            break   # Sai do loop

        except KeyError:
            # O usuário digitou um item que não está no menu, então ignoramos
            pass

# Executa a função principal
if __name__ == "__main__":
    main()
