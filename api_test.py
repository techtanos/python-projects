import urllib.request
import json
url = "https://api.exchangerate-api.com/v4/latest/MAD"
response = urllib.request.urlopen(url)
data = json.loads(response.read())
usd_rate = data['rates']['USD']
eur_rate = data['rates']['EUR']
print(f"1 MAD = {usd_rate:.4f} USD")
print(f"1 MAD = {eur_rate:.4f} EUR")
