import sys
import requests

def main():
    # 1. Validação do argumento de linha de comando (esta parte já estava correta)
    if len(sys.argv) != 2:
        sys.exit("Missing command-line argument")
    try:
        n_bitcoins = float(sys.argv[1])
    except ValueError:
        sys.exit("Command-line argument is not a number")

    # 2. Busca na API (versão simplificada e sem chave)
    try:
        # Usando o link público e direto para o Bitcoin, que não requer chave.
        url = "https://rest.coincap.io/v3/assets?apiKey=15546b177c34b5331707ba0b4b8d3195b4780b676d04d55cb82fc6b4d84325cc"

        response = requests.get(url)
        # Verifica se a requisição foi bem-sucedida (ex: status 200)
        response.raise_for_status()

        data = response.json()

        # Caminho direto para o preço na estrutura da CoinCap
        price_str = data['data']['priceUsd']
        price = float(price_str)

    except requests.RequestException:
        sys.exit("Request to API failed")
    except (KeyError, TypeError, ValueError):
        # Captura erros se a estrutura do JSON for inesperada ou o preço não for um número
        sys.exit("Failed to parse API data")

    # 3. Cálculo e impressão do resultado final (esta parte já estava correta)
    total_cost = n_bitcoins * price
    print(f"${total_cost:,.4f}")


if __name__ == "__main__":
    main()
