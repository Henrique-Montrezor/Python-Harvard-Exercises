import random

def main():
    # Pede o nível ao usuário UMA ÚNICA VEZ no início do programa.
    level = get_level()
    score = 0

    # Laço principal que gera 10 problemas matemáticos.
    for _ in range(10):
        # O contador de erros é zerado para cada nova pergunta.
        errors = 0

        # Gera dois números com base no nível que já foi escolhido.
        num_x = generate_integer(level)
        num_y = generate_integer(level)
        result = num_x + num_y

        # Laço interno que permite até 3 tentativas por pergunta.
        while errors < 3:
            try:
                # Pede a resposta ao usuário.
                resposta = int(input(f"{num_x} + {num_y} = "))

                # Se a resposta for correta, aumenta o placar e sai do laço de tentativas.
                if resposta == result:
                    score += 1
                    break
                # Se a resposta for incorreta, imprime "EEE" e conta um erro.
                else:
                    errors += 1
                    print("EEE")

            # Se o usuário digitar algo que não seja um número, conta como um erro.
            except ValueError:
                errors += 1
                print("EEE")

        # Se o laço de tentativas acabou por excesso de erros (3), mostra a resposta correta.
        if errors == 3:
            print(f"{num_x} + {num_y} = {result}")

    # No final do jogo, exibe o placar final.
    print(f"Score: {score}")


def get_level():
    """Pede ao usuário um nível (1, 2 ou 3) e o retorna, repetindo se a entrada for inválida."""
    while True:
        try:
            level = int(input("Level: "))
            # Verifica se o nível está entre as opções válidas.
            if level in [1, 2, 3]:
                return level
        except ValueError:
            # Se a entrada não for um número, o laço continua.
            pass


def generate_integer(level):
    """Gera um inteiro aleatório com base no nível fornecido como argumento."""
    if level == 1:
        # Dígito único (0-9)
        return random.randint(0, 9)
    elif level == 2:
        # Dois dígitos (10-99)
        return random.randint(10, 99)
    else: # level == 3
        # Três dígitos (100-999)
        return random.randint(100, 999)


# Garante que a função main() seja chamada quando o script é executado.
if __name__ == "__main__":
    main()
