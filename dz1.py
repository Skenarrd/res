import math
import pylab
import numpy
from matplotlib import mlab # Вспомогательные ф-ии
import json
import os
import os.path
import shutil
#from pathlib import Path

 
def func(x):
    return (100 * (abs(1 - (0.01 * (x ** 2))) ** 0.5) + 0.01 * abs(x + 10))
 
# Интервал изменения по оси X
minX = -15
maxX = 5
 
# Шаг между точками
iX = 0.1
 
# Список координат по оси X на отрезке от minX до maxX, включая концы
xlist = numpy.arange(minX, maxX, iX)

# Значение функции в заданных точках
ylist = [func(x) for x in xlist]
'''
print(xlist)
print(ylist, sep = '\n')
'''

# Одномерный график
pylab.plot (xlist, ylist)
# Окно с нарисованным графиком
pylab.show()


fileData = {
    'x': list(xlist),
    'y': ylist
}

# Запись результатов в файл
with open('result.json', 'w') as file:
    data = json.dumps(fileData, indent = 2) # кол-во отступов
    file.write(data)

# Создание директория с именем 'results'
if not os.path.exists('results'):
    os.mkdir('results')
'''
x = os.getcwd
for file in list(os.path.join(x, '*.json')): 
    shutil.move(file, 'results')
# TypeError: expected str, bytes or os.PathLike object, not builtin_function_or_method
'''

# Перемещение файла с результатом в созданный директорий


'''
folder_path = Path('mod_ED', '1')
file_path = folder_path / 'result.json'
new_folder_path = Path('1', 'results')
new_file_path = new_folder_path / 'result.json'
if not os.path.isfile(file_path):
    shutil.move(
    file_path, new_file_path
    )
FileNotFoundError: [Errno 2] 
No such file or directory: 'mod_ED\\1\\result.json'
Почему в окне выводятся двойные слэши при указании пути?
'''

'''
home_path = Path.home()
abs_file_path = (home_path, 'Desktop', 'mod_ED', '1', 'result')
new_file_path = (abs_file_path, )
'''

if not os.path.isfile('C:/Users/KIR The Programmer/Desktop/mod_ED/1/results/result.json'):
    shutil.move(
    'C:/Users/KIR The Programmer/Desktop/mod_ED/1/result.json', 
    'C:/Users/KIR The Programmer/Desktop/mod_ED/1/results/result.json'
    )

