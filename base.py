import tkinter as tk
import tkinter.filedialog as filedialog
import matplotlib.pyplot as plt


def choose_file():
    # Открываем окно выбора файла
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename()

    if file_path:
        # Считываем данные из выбранного файла
        with open(file_path, 'r') as f:
            lines = f.readlines()

        # Получаем не более 10 последних точек
        num_points = min(10, len(lines))
        data = [(line.strip().split(': ')[0], float(line.strip().split(': ')[1]))
                for line in lines[-num_points:]]

        # Строим график
        x = [point[0] for point in data]
        y = [point[1] for point in data]
        plt.plot(x, y)
        plt.xlabel('Время')
        plt.ylabel('Цена')
        plt.title('График цены криптовалюты')
        plt.show()


# Запускаем окно выбора файла
choose_file()
