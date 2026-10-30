import requests
from API_KEY import EXCHANGE_API_KEY

URL = f"https://v6.exchangerate-api.com/v6/{EXCHANGE_API_KEY}/latest/USD"
HEADERS = {"User-Agent": "ProjeckBot/1.0"}

response = requests.get(URL, headers=HEADERS, timeout=10)
data = response.json()
rates = data["conversion_rates"]



while True:
        user_input = input("Введите сумму (или 'q' для выхода): ").strip()
        if user_input.lower() == 'q':
            print("До встречи!")
            break
        else:
            amount = float(user_input)
            from_currency = input("Введите откуда (в формате USD): ").upper()
            to_currency = input("Введите куда (в формате USD): ").upper()

            rate_from = rates.get(from_currency)
            rate_to = rates.get(to_currency)
        
            if rate_from is None:
                print(f"Ошибка: валюты {from_currency} не существует!")
            elif rate_to is None:
                print(f"Ошибка: валюты {to_currency} не существует!")
            else:
            
                result = (amount / rate_from) * rate_to #ФОРМУЛА

                print(f"{amount} {from_currency} = {round(result, 2)} {to_currency}")