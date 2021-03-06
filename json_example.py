# json - текстовый формат обмена данными

import json
# создадим объект json. Сделаем это из дикта (dict)

dict_ex = {'Brand':'Volvo', 'Price': 1.5, 'Vol': 2.0}

# dump, dumps - метод, которым можно привести к типу json
# dumps - используется в рамках одного проекта
# dump - используется, если нужно, например, передать данные в файл и использовать их потом еще где-то

# мы можем получить объект типа json следующим способом

dict_to_json = json.dumps(dict_ex)      # вызываем из пакета json метод dumps и передаем на вход ему информацию (dict_ex)
print(type(dict_to_json), dict_to_json)
#---> <class 'str'> {"Brand": "Volvo", "Price": 1.5, "Vol": 2.0}
# мы видим, что данные сконвертировались. Методом dumps из пакета json словарь (dict_ex) стал строкой (dict_to_json).
# теперь мы не можем обращаться ни по ключу, ни использровать какие-то медоды (функции) из dict
# Сереализация данных. Мы только что сериализовали данные. Т.е. перевод данных в формат, который удобен для всех.
# Теперь мы можем его, например, записать в файл:

with open('dict_to_json.txt', 'w') as f:    # с помощью менеджера контекста открываем файл dict_to_json на запись
    json.dump(dict_ex, f)                   # с помощью медода dump объекта json запишем данные в файл

# теперь наоборот, прочитаем этот файл (dict_to_json.txt) и создадим из него словарь для дальнейшей обработки:
# load, loads - для обратной конвертации
with open('dict_to_json.txt') as f:
    data = json.load(f)     # в скобках указывается только файл
print(type(data), data)

# проверим теперь метод loads:

data_1 = json.loads(dict_to_json)   # подадим на вход объект dict_to_json
print(type(data_1), data_1)

# Реальный пример работы с данными json. Ответ по API

import requests

response = requests.get("https://jsonplaceholder.typicode.com/todos")
data_2 = json.loads(response.text)
print(data_2)


