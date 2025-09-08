def main():
    """
    Função principal: Pede o nome de uma fruta ao usuário e, se estiver no
    catálogo, imprime suas calorias.
    """
    # 1. Cria um dicionário com as informações nutricionais.
    #    As chaves (nomes das frutas) estão em minúsculas para facilitar a busca.
    catalogo_frutas = {
        "apple": 130,
        "avocado": 50,
        "banana": 110,
        "cantaloupe": 50,
        "grapefruit": 60,
        "grapes": 90,
        "honeydew melon": 50,
        "kiwifruit": 90,
        "lemon": 15,
        "lime": 20,
        "nectarine": 60,
        "orange": 80,
        "peach": 60,
        "pear": 100,
        "pineapple": 50,
        "plums": 70,
        "strawberries": 50,
        "sweet cherries": 100,
        "tangerine": 50,
        "watermelon": 80,
    }

    # 2. Pede o nome da fruta ao usuário.
    item_usuario = input("Item: ")

    # 3. Converte a entrada do usuário para letras minúsculas.
    #    Isso torna a busca insensível a maiúsculas (ex: "Apple" e "apple" funcionarão).
    item_formatado = item_usuario.lower()

    # 4. Verifica se o item formatado existe como uma chave no dicionário.
    if item_formatado in catalogo_frutas:
        # 5. Se existir, imprime o valor de calorias correspondente.
        #    catalogo_frutas[item_formatado] acessa o valor associado à chave.
        print(f"Calories: {catalogo_frutas[item_formatado]}")

# Executa a função main
main()
