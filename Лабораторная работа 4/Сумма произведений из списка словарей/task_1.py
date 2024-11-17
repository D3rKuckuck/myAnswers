# 8wwr5oMkdH1O/kdMuQqz2c+Bw+rIlpFzoTyr3v/RVk=
import json
import random
import math


def get_sum_of_products(file_path):
    try:
        with open(file_path, 'r') as f:
            data = json.load(f)

    except:  # Если файл полностью пуст/не существует или некорректен
        print("Файл задан неверно, не существует или пуст и будет перезаписан")
        # Запишем случайные значения в файл
        with open(file_path, 'w') as f:
            json_list = []
            range_ = random.randint(0, 10)
            for _ in range(range_):
                score = random.uniform(0, 10)
                weight = random.uniform(0, 10)
                json_list += [{"score": score, "weight": weight}]
            json_list = json.dumps(json_list, indent=4)
            f.write(json_list)  # Так как строка уже в нужном формате
        with open(file_path, 'r') as f:
            data = json.load(f)
    list_of_products = []
    for dicts in data: # Список произведений
        list_of_products += [math.prod(value for key, value in dicts.items())]
    sum_of_products = round(sum(list_of_products), 3)
    return sum_of_products


file_path = "input.json"
print('Сумма произведений пар значений:', get_sum_of_products(file_path))
