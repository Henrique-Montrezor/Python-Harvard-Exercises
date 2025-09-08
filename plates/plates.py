def main():
    """
    Função principal: pede uma placa ao usuário e imprime se é válida ou não.
    """
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    """
    Verifica se uma string 's' corresponde a todas as regras de uma placa de vaidade.
    Retorna True se for válida, False caso contrário.
    """
    # Regra 1: Verifica o comprimento (entre 2 e 6 caracteres)
    if not (2 <= len(s) <= 6):
        return False

    # Regra 2: Verifica se os dois primeiros caracteres são letras
    if not s[0].isalpha() or not s[1].isalpha():
        return False
    # Alternativa mais curta: if not s[:2].isalpha():

    # Regra 5: Verifica se não há pontuação, espaços, etc.
    # .isalnum() verifica se todos os caracteres são letras OU números.
    if not s.isalnum():
        return False

    # Itera pela string para verificar as regras sobre números
    for i in range(len(s)):
        # Verifica se o caractere atual é um dígito
        if s[i].isdigit():
            # Se for um dígito, encontramos o início da parte numérica.

            # Regra 4: O primeiro número não pode ser '0'
            if s[i] == '0':
                return False

            # Regra 3: Os números devem vir no final.
            # A partir deste ponto, todos os caracteres restantes devem ser números.
            # Criamos uma "fatia" (slice) do resto da string: s[i:]
            if not s[i:].isdigit():
                return False

            # Se as regras dos números foram verificadas e passaram, podemos parar o laço,
            # pois já validamos a parte numérica da placa.
            break

    # Se a função executou até aqui sem retornar False, a placa é válida.
    return True


# Executa a função main
main()
