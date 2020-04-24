'''
Работа с текстовыми файлами
'''

'''
# Откроем файл data / простое считывание
f = open('data')
content = f.read()  # считаем содержимое
print(content)
f.close()   # файл нужно закрыть
'''

'''
# откроем файл в режиме w - на запись. ПРИ ЭТОМ ВСЕ СОДЕРЖИМОЕ УДАЛИТСЯ!!!
f = open('data', 'w')
content = f.read()  # считаем содержимое
print(content)
f.close()   # файл нужно закрыть
'''

'''
# считывание файла построчно:
f = open('data')
for line in f:
    print(line)
f.close()   # файл нужно закрыть
'''
'''
# Менеджер контекста (close уже не нужен, файл закроется автоматически) - удобно
with open('data') as f:
    for line in f:
        print(line)
'''

'''
# Запись в файл
with open('data_new', 'w') as f:
    f.write('This is new file')
'''

# Запись в файл построчно:
data = ['1\n', '2\n', '3\n']    # элементы списка должны быть строками! \n - перенос на следующую строку!
with open('data_new', 'w') as f:
    f.writelines(data)

# Считывание одной строки:
with open('data') as f:
    line = f.readline()
    print(line)




