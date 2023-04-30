import os

# Название папки, которую мы хотим создать
folder_name = 'Crypta_data'

# Создаем новую папку
try:
    os.mkdir(folder_name)
except FileExistsError:
    pass

# Путь к папке
folder_path = os.path.join(os.getcwd(), folder_name)

# Создаем файл для сообщений о понижении цены
filename = os.path.join(folder_path, 'falling_prices.txt')

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

# Сообщаем о понижении цены


def report_falling_price(symbol, price, threshold):
    prev_price = float(price) / (1 + threshold)
    diff = float(price) - prev_price
    percentage_change = (diff / prev_price) * 100
    if percentage_change <= -10:
        data = f'Цена криптовалюты {symbol} упала на {percentage_change:.2f}% с {prev_price:.2f} до {price:.2f}'
        write_data_to_file(filename, data)


# Пример использования
# Отчет не будет создан, т.к. изменение цены меньше 10%
report_falling_price('BTCUSDT', '50000.00', 0.05)
# Отчет будет создан, т.к. изменение цены больше 10%
report_falling_price('ETHUSDT', '4000.00', 0.05)
