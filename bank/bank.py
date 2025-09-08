# Pede a saudação ao usuário e formata para minúsculas e sem espaços extras
greeting = input("Greeting: ").lower().strip()

# Verifica as condições na ordem correta (do mais específico para o mais geral)
if greeting.startswith("hello"):
    print("$0")
elif greeting.startswith("h"):
    print("$20")
else:
    print("$100")
