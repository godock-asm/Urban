# Арзамасцев Сергей.

# Домашнее задание по теме "Основные типы данных и знакомство с переменными"

name_kurs = 'Курс: Python'
quantity_dz = 12
quantity_h = 1.5
time = 1.5/12
print(name_kurs,',' 'всего задач:', quantity_dz,',' 'затрачено часов:', quantity_h,',' 'среднее время выполнения', time,'часа.')

# Исправление ошибки по домашнему заданию "Основные типы данных и знакомство с переменными"

name_kurs = 'Курс: Python'
quantity_dz = 12
quantity_h = 1.5
time = quantity_h/quantity_dz
print(name_kurs,',' 'всего задач:', quantity_dz,',' 'затрачено часов:', quantity_h,',' 'среднее время выполнения',
      time,'часа.')

# Домашнее задание по теме "Определение типа данных"
# Практическая работа по уроку "Динамическая типизация"
# Цель: Написать программу на языке Python, используя Pycharm, для демонстрации динамической типизации.

name = 'Сергей'
print('Name:', name)
age = 64
print('Age:', age)
age = (64+1)
print('New age:', age)
is_student = 1
is_student = bool(is_student)
print('Is Student:', is_student )

# Домашнее задание по теме "Строковый тип данных" №1
# Цель: Научиться работать со строками и индексацией строк в Python.

example='Арзамасцев'
print(example[0])
print(example[-1])
print(example[3:8])
print(example[-1::-1])
print(example[1:10:2])