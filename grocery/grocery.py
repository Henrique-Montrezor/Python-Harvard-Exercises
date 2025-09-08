def main():
    """
    Cria uma lista de compras a partir da entrada do usuário,
    conta os itens e exibe a lista final ordenada.
    """
    # Dicionário para armazenar itens (chave) e suas contagens (valor)
    grocery_list = {}

    # Loop infinito para capturar a entrada do usuário
    while True:
        try:
            # Pede um item e o converte para maiúsculas para padronização
            item = input().upper()

            # Adiciona o item à lista ou incrementa sua contagem
            if item in grocery_list:
                grocery_list[item] += 1
            else:
                grocery_list[item] = 1

        except EOFError:
            # O usuário pressionou Ctrl+D, sinalizando o fim da entrada
            print() # Imprime uma linha em branco para melhor formatação no terminal

            # Itera sobre as chaves do dicionário em ordem alfabética
            for item in sorted(grocery_list):
                # Imprime a contagem e o nome do item
                print(f"{grocery_list[item]} {item}")

            # Sai do loop infinito para encerrar o programa
            break

# Executa a função principal
if __name__ == "__main__":
    main()
