def main():
    """
    Função principal: Pede o custo da refeição e a porcentagem da gorjeta,
    calcula o valor da gorjeta e o imprime.
    """
    dollars = dollars_to_float(input("How much was the meal? "))

    percent = percent_to_float(input("What percentage would you like to tip? "))

    tip = dollars * percent

    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    """
    Converte uma string no formato $##.## para um float.
    Exemplo: "$50.00" -> 50.0
    """
    d_without_dollar_sign = d.replace("$", "")
    return float(d_without_dollar_sign)


def percent_to_float(p):
    """
    Converte uma string de porcentagem no formato ##% para um float.
    Exemplo: "15%" -> 0.15
    """
    p_without_percent_sign = p.replace("%", "")
    return float(p_without_percent_sign) / 100


# Executa a função main
main()
