import requests
import time
import os

MAX_ROWS = 990
DELETE_ROWS = 400

# Название папки, в которой будет находиться файл
folder_name = 'Crypta_data'

# Путь к папке
folder_path = os.path.join(os.getcwd(), folder_name)

# Создаем файл для сообщений о повышении цены
rising_filename = os.path.join(folder_path, 'rising_prices.txt')

# Записываем данные в файл


def write_data_to_file(filename, data):
    with open(filename, 'a+') as f:
        f.seek(0)
        lines = f.readlines()
        if len(lines) >= 10:
            f.seek(0)
            f.truncate()
            lines = lines[-9:]
        for line in lines:
            f.write(line)
        f.write(data + '\n')


while True:
    # Считываем данные с Binance API
    response = requests.get('https://api.binance.com/api/v3/ticker/24hr')
    data = response.json()

    # Проверяем изменение цены на 10% и записываем данные в файл
    for currency in data:
        symbol = currency['symbol']
        price = float(currency['lastPrice'])
        price_change_percent = float(currency['priceChangePercent'])

        if price_change_percent >= 10.0:
            data = f'Цена криптовалюты {symbol} выросла на {price_change_percent}%'
            print(data)
            write_data_to_file(rising_filename, data)

    # Обновляем данные каждую секунду
    time.sleep(60)
