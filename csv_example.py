import csv

'''
функция csv.reader
функция csv.writer
класс csv.Dictwriter
класс csv.DictReader
'''
# 1) csv.writer

car_data = [['brand', 'price', 'year'], ['Volvo', 1.5, 2017], ['Lada', 0.5, 2018], ['Audi', 2.0, 2018]]
# будем использовать менеджер контекста, чтобы записать файл
with open('example.csv', 'w', newline='') as f:     # newline='' - чтобы не образовывалась пустая строка после каждой строки
    writer = csv.writer(f, delimiter = '&')       # создаем объект writer. На вход укажем параметр, что запись происходит в f. delimiter = '&' - разделитель
    writer.writerows(car_data)  # записываем в объект writer. Записываем построчно (writerows())
print('Writing complete')


# Теперь считаем файл, который только что создали. Для этого потребуетс функция reader
# 2) csv.reader
with open('example.csv') as f:  # по умолчанию будет режим чтения
    reader = csv.reader(f, delimiter = '&')        # создаем объект reader
    # далее в цикле выведем построчно содержимое example.csv
    for row in reader:
        print(row)  # row - строка

# 3) csv.Dictwriter
# создадим словарь (два поля: имя и возраст) из трех срок:
data_dict = [{'Name': 'Dima', 'age': 28},
             {'age': 29, 'Name': 'Kate'},
             {'Name': 'Mike', 'age': 31}]
fieldnames = ['Name', 'age']    # fieldnames - имена колонок. Он будет искать в словаре data_dict и записывать в нужную колонку.
# вызываем менеджер контекста
with open('example_1.csv', 'w', newline='') as f:
    writer = csv.DictWriter(f, delimiter = '&', fieldnames = fieldnames)
    # далее нужно прописать поля. Что будут колонки Name и age. Для этого используется метод writeheader
    writer.writeheader()
    # мы прописали заголовки, теперь будем насыщать файл информацией:
    # пробежимся по списку. Зададим цикл по длине списка:
    for i in range(len(data_dict)):
        # будем использовать метод writerow()
        writer.writerow(data_dict[i])

# 4) csv.DictReader
# с помощью DictReader считаем файл example_1.csv, который мы получили
with open('example_1.csv') as f:
    reader = csv.DictReader(f, delimiter = '&')
    # считывание происходит по рядам
    for row in reader:
        print(dict(row))

# ДЛЯ АНАЛИЗА ФАЙЛОВ ИСПОЛЬЗУЮТ PANDAS:

#import pandas as pd

# в pandas ключевым объектом является DataFrame
#DataFrame_from_csv = pd.read_csv('example_1.csv',sep = '&')  # считали example_1.csv (где sep = '&' - это разделитель) и поместили это в объект DataFrame_from_csv
#print(type(DataFrame_from_csv))
#print(DataFrame_from_csv)





