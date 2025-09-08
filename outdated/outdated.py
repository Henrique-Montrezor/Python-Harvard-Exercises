def main():
    """
    Solicita uma data ao usuário em formato americano, valida-a,
    e a imprime no formato ISO 8601 (YYYY-MM-DD).
    """
    months = [
        "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"
    ]

    while True:
        date_str = input("Date: ").strip()

        # Tenta o formato MM/DD/YYYY
        try:
            m_str, d_str, y_str = date_str.split("/")
            m, d, y = int(m_str), int(d_str), int(y_str)
            if 1 <= m <= 12 and 1 <= d <= 31:
                break # Data válida, sai do loop
        except ValueError:
            # Se a primeira tentativa falhar, tenta o segundo formato
            try:
                # Tenta o formato Mês Dia, Ano
                month_name, d_str, y_str = date_str.split(" ")

                # Ignora se não houver vírgula após o dia
                if not d_str.endswith(","):
                    continue

                d_str = d_str.replace(",", "") # Remove a vírgula
                d, y = int(d_str), int(y_str)

                # Converte o nome do mês para número
                m = months.index(month_name) + 1

                if 1 <= d <= 31:
                    break # Data válida, sai do loop
            except (ValueError, KeyError):
                # Se ambos os formatos falharem, o loop continua e pede a data novamente
                pass

    # Imprime a data no formato ISO 8601
    # :02 garante que o número terá 2 dígitos (ex: 9 -> 09)
    print(f"{y}-{m:02}-{d:02}")


if __name__ == "__main__":
    main()
