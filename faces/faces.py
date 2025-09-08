def main():

    texto_original = input("")

    texto_convertido = converter(texto_original)

    print(texto_convertido)

def converter(frase):
    """
    Recebe uma string, substitui os emoticons :) e :( por emojis
    e retorna a nova string.
    """

    frase_modificada = frase.replace(":)", "🙂")

    frase_final = frase_modificada.replace(":(", "🙁")

    return frase_final

main()
