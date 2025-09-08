import re
import sys

def main():
    # Pede o texto ao usuário e imprime a contagem
    print(count(input("Text: ")))

def count(s):
    """
    Conta quantas vezes a palavra 'um' aparece em uma string,
    ignorando maiúsculas/minúsculas e garantindo que seja uma palavra inteira.
    """
    # re.findall encontra todas as ocorrências que correspondem ao padrão.
    # \b -> é um limite de palavra (word boundary). Isso garante que estamos
    #       procurando por "um" como uma palavra inteira, e não como parte
    #       de outra palavra (ex: "yummy").
    # re.IGNORECASE -> faz a busca ignorar se as letras são maiúsculas ou minúsculas.
    um_list = re.findall(r"\bum\b", s, re.IGNORECASE)

    # O número de ocorrências é o tamanho da lista retornada por findall.
    return len(um_list)

if __name__ == "__main__":
    main()
