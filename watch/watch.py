import re
import sys

def main():
    # Pede ao usuário o código HTML do iframe
    html = input("HTML: ")
    # Imprime o link curto do YouTube ou "None" se não for encontrado
    print(parse(html))

def parse(html):
    """
    Extrai o ID do vídeo de um iframe do YouTube e retorna um link curto.
    Retorna o link no formato https://youtu.be/ID ou None se não encontrar.
    """
    # Usamos uma expressão regular para encontrar o padrão do URL do YouTube
    # r'...' -> Raw string para evitar problemas com barras invertidas
    # "https?://" -> Corresponde a http:// ou https://
    # (?:www\.)? -> Grupo de não captura. Corresponde a "www." opcionalmente
    # youtube\.com/embed/ -> Corresponde ao URL base de embed do YouTube
    # ([a-zA-Z0-9_]+) -> Grupo de captura para o ID do vídeo. O ID pode ter letras, números e _.
    match = re.search(r"<iframe.*?src=\"https?://(?:www\.)?youtube\.com/embed/([a-zA-Z0-9_]+)\".*?></iframe>", html)

    # Se a expressão regular encontrar um padrão correspondente
    if match:
        # O ID do vídeo é o primeiro (e único) grupo de captura
        video_id = match.group(1)
        return f"https://youtu.be/{video_id}"
    else:
        # Se nenhum padrão for encontrado, retorna None
        return None

if __name__ == "__main__":
    main()
