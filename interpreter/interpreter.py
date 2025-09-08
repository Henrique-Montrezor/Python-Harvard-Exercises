# Pede a expressão ao usuário
expression = input("Expression: ")

# Separa a string em três partes usando o espaço como delimitador
x, operator, z = expression.split(" ")

# Converte as partes numéricas de string para inteiro
num_x = int(x)
num_z = int(z)

# Realiza a operação correspondente
if operator == '+':
    result = num_x + num_z
elif operator == '-':
    result = num_x - num_z
elif operator == '*':
    result = num_x * num_z
elif operator == '/':
    result = num_x / num_z

# Imprime o resultado formatado como um float com uma casa decimal
print(f"{result:.1f}")
