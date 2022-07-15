import sys
from dateutil import parser
import requests


try:
    currency = sys.argv[1]
except IndexError:
    currency = input("Podaj Walute: ")
currency = currency.upper()
try:
    date = sys.argv[2]
except IndexError:
    date = input("Podaj Date: ")


try:
    format_of_date = parser.parse(date)
except ValueError:
    print("Zły format daty")
    sys.exit(1)
date = format_of_date.strftime("%Y-%m-%d")
url = f"http://api.nbp.pl/api/exchangerates/rates/a/{currency}/{date}/?format=json"
r = requests.get(url)
if r.status_code == 404:
    print("Brak Danych")
    sys.exit(2)
if not r.ok:
    print("ERROR")
    sys.exit(3)

json = r.json()
try:
    rate = json["rates"][0]["mid"]
except:
    print("Invalid server response")

print("KALKULATOR WALUT")
print(f"1 {currency} = {rate} zł z dnia: {date}")