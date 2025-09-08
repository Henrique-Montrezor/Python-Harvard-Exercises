import sys
import os
from PIL import Image, ImageOps

def main():
    # Passo 1: Validar os argumentos da linha de comando
    verificar_argumentos()

    # Define os nomes dos arquivos de entrada e saída
    arquivo_entrada = sys.argv[1]
    arquivo_saida = sys.argv[2]

    # Passo 2: Validar as extensões dos arquivos
    verificar_extensoes(arquivo_entrada, arquivo_saida)

    try:
        # Passo 3: Abrir as imagens
        # Abre a imagem da camiseta que servirá de "molde"
        camisa = Image.open("shirt.png")
        # Abre a foto do usuário que será o "fundo"
        foto_usuario = Image.open(arquivo_entrada)

        # Pega o tamanho exato da imagem da camiseta
        tamanho = camisa.size

        # Passo 4: Redimensionar e cortar a foto do usuário
        # ImageOps.fit garante que a foto terá o mesmo tamanho da camiseta,
        # mantendo a proporção e cortando o que for necessário.
        foto_ajustada = ImageOps.fit(foto_usuario, tamanho)

        # Passo 5: Sobrepor a camiseta na foto ajustada
        # O método .paste() cola uma imagem sobre a outra.
        # O segundo argumento 'camisa' atua como uma "máscara",
        # garantindo que a transparência do PNG seja respeitada.
        foto_ajustada.paste(camisa, camisa)

        # Passo 6: Salvar o resultado final
        foto_ajustada.save(arquivo_saida)

    except FileNotFoundError:
        # Trata o erro caso o arquivo de entrada não exista
        sys.exit("Input does not exist")


def verificar_argumentos():
    """Verifica se o número de argumentos na linha de comando é correto."""
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")


def verificar_extensoes(entrada, saida):
    """Verifica se as extensões dos arquivos de entrada e saída são iguais e válidas."""
    # Lista de extensões permitidas
    extensoes_validas = [".jpg", ".jpeg", ".png"]

    # os.path.splitext() divide o nome do arquivo em (nome, .extensão)
    ext_entrada = os.path.splitext(entrada)[1].lower()
    ext_saida = os.path.splitext(saida)[1].lower()

    if ext_entrada not in extensoes_validas:
        sys.exit("Invalid input")

    if ext_saida not in extensoes_validas:
        sys.exit("Invalid output")

    if ext_entrada != ext_saida:
        sys.exit("Input and output have different extensions")


# Garante que a função main() seja chamada ao executar o script
if __name__ == "__main__":
    main()
