expression = input("Expression: ")

x, operator, z = expression.split(" ")

num_x = int(x)
num_z = int(z)

if operator == '+':
    result = num_x + num_z
elif operator == '-':
    result = num_x - num_z
elif operator == '*':
    result = num_x * num_z
elif operator == '/':
    result = num_x / num_z

print(f"{result:.1f}")
