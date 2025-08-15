import sys
import requests

def main():
    if len(sys.argv) != 2:
        sys.exit("Missing command-line argument")
    try:
        n_bitcoins = float(sys.argv[1])
    except ValueError:
        sys.exit("Command-line argument is not a number")

    try:
        url = "https://rest.coincap.io/v3/assets?apiKey=15546b177c34b5331707ba0b4b8d3195b4780b676d04d55cb82fc6b4d84325cc"

        response = requests.get(url)
        response.raise_for_status()

        data = response.json()

        price_str = data['data']['priceUsd']
        price = float(price_str)

    except requests.RequestException:
        sys.exit("Request to API failed")
    except (KeyError, TypeError, ValueError):
        sys.exit("Failed to parse API data")

    total_cost = n_bitcoins * price
    print(f"${total_cost:,.4f}")


if __name__ == "__main__":
    main()
