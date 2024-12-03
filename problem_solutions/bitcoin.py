import sys
import requests

try:
    r = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    file = r.json()
    rate = float(file["bpi"]["USD"]["rate_float"])
except requests.RequestException:
    pass

if len(sys.argv) == 1:
    print("Missing command-line argument")
    sys.exit(1)
elif len(sys.argv) == 2:
    if float(sys.argv[1]) is False:
        print("Command-line argument is not a number")
        sys.exit(1)
    else:
        amount = float(sys.argv[1]) * rate
        print(f"${amount:,.4f}")
