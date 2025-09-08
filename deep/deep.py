# Pede a entrada do usuário e a formata imediatamente
answer = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ").lower().strip()

# Verifica se a resposta formatada corresponde a uma das opções válidas
if answer == "42" or answer == "forty-two" or answer == "forty two":
    print("Yes")
else:
    print("No")

