задача_1:
import numpy as np
import matplotlib.pyplot as plt

# Создание массива значений x от 0 до 2π
x = np.linspace(0, 2 * np.pi, 1000)

# Вычисление значений y = sin(x)
y = np.sin(x)

# Построение графика
plt.plot(x, y)

# Добавление подписей осей и заголовка
plt.xlabel('x')
plt.ylabel('y')
plt.title('График функции y = sin(x)')

# Добавление сетки
plt.grid(True)

# Отображение графика
plt.show()





задача_2:

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 2 * np.pi, 1000)

y_1 = np.sin(x)
y_2 = np.cos(x)
y_3 = np.tan(x)
plt.plot (x,y_1, y_2, y_3)

plt.xlabel('x')
plt.ylabel('y')
plt.title('График функции y_1 = sin(x)')
plt.title('График функции y_2 = cos(x)')
plt.title('График функции y_3 = tan(x)')
plt.grid(True)
plt.show()

задача_3:
import matplotlib.pyplot as plt
import numpy as np

# Генерируем случайные данные
data = np.random.randn(1000)

# Создаем гистограмму
plt.hist(data, bins=30, alpha=0.7, color='blue', edgecolor='black')

# Добавляем заголовок и метки осей
plt.title('Гистограмма случайных данных')
plt.xlabel('Значение')
plt.ylabel('Частота')

# Показываем график
plt.show()

задача_4:

import matplotlib.pyplot as plt

x = ['Яблоки', 'Бананы', 'Апельсин', 'Груши',]
y = [10, 15, 7, 12]

plt.bar(x,y)

# Добавление подписей осей и заголовка
plt.xlabel('название')
plt.ylabel('Количество')
plt.title('Количество фруктов на складе')

# Отображение диаграммы
plt.show()



