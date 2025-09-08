def main():
    """
    Função principal: Pede a massa ao usuário e imprime a energia correspondente.
    """
    massa_kg = int(input("m: "))

    velocidade_luz = 300000000

    energia_joules = massa_kg * (velocidade_luz ** 2)

    print(f"E: {energia_joules}")


# Executa a função main para iniciar o programa
main()
