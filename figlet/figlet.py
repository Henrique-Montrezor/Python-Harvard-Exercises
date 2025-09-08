import sys
import random
from pyfiglet import Figlet

def main():
    """
    Renderiza o texto em uma fonte FIGlet especificada ou aleatória.
    """
    figlet = Figlet()
    font_list = figlet.getFonts()

    if len(sys.argv) == 1:
        try:
            font_name = random.choice(font_list)
            figlet.setFont(font=font_name)
        except IndexError:
            sys.exit("Nenhuma fonte encontrada.")

    elif len(sys.argv) == 3 and (sys.argv[1] == "-f" or sys.argv[1] == "--font"):
        font_name = sys.argv[2]
        if font_name not in font_list:
            sys.exit("Fonte inválida")
        figlet.setFont(font=font_name)

    else:
        sys.exit("Uso inválido")

    text_to_render = input("Input: ")

    print("Output:")
    print(figlet.renderText(text_to_render))

if __name__ == "__main__":
    main()
