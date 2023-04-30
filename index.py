import requests
import time
import os

MAX_ROWS = 990
DELETE_ROWS = 400

while True:
    # Считываем данные с Binance API
    response = requests.get('https://api.binance.com/api/v3/ticker/24hr')
    data = response.json()

    # Записываем данные в файлы
    for currency in data:
        symbol = currency['symbol']
        price = currency['lastPrice']

        filename = f'{symbol}.txt'
        with open(filename, 'a+') as f:
            # Ограничиваем количество строк в файле
            f.seek(0)
            lines = f.readlines()
            if len(lines) >= MAX_ROWS:
                f.seek(0)
                f.truncate()
                lines = lines[-MAX_ROWS + 1:]
            for line in lines:
                f.write(line)
            f.write(f'{time.strftime("%Y-%m-%d %H:%M:%S")}: {price}\n')

        # Удаляем старые записи, если их количество превышает MAX_ROWS - DELETE_ROWS
        with open(filename, 'r') as f:
            lines = f.readlines()
        if len(lines) > MAX_ROWS - DELETE_ROWS:
            with open(filename, 'w') as f:
                f.writelines(lines[-(MAX_ROWS - DELETE_ROWS):])

    # Обновляем данные каждую секунду
    time.sleep(60)
