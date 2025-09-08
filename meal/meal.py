def main():
    # Pega o horário do usuário
    time_str = input("What time is it? ")
    # Converte o horário (string) para um número (float) usando a função auxiliar
    time_float = convert(time_str)

    # Verifica em qual intervalo de refeição o horário se encaixa
    if 7.0 <= time_float <= 8.0:
        print("breakfast time")
    elif 12.0 <= time_float <= 13.0:
        print("lunch time")
    elif 18.0 <= time_float <= 19.0:
        print("dinner time")

def convert(time):
    # Separa a string "HH:MM" em horas e minutos
    hours, minutes = time.split(":")
    # Converte os minutos em uma fração da hora (ex: 30 min = 0.5 hora)
    minutes_as_hour = float(minutes) / 60
    # Retorna o total de horas como um float
    return float(hours) + minutes_as_hour

# Garante que a função main() seja executada quando o script é rodado
if __name__ == "__main__":
    main()
