# mNjKfoa8B
import json
import csv
from pprint import pprint


def csv_into_jason(file_path, converted_file_path):
    with open(file_path, 'r') as f:
        data = [line for line in csv.reader(f)]  # Разделители уже установлены по умолчанию
    keys_list = data[0]
    values_list = data[1:]
    for i1, line in enumerate(values_list):
        for i2, value in enumerate(line):
            # Сохраняем значения соответственно возможному
            # типу данных
            if '.' in value:
                try: values_list[i1][i2] = float(value)
                except: pass
            elif value == 'True' or value == 'False':
                values_list[i1][i2] = bool(value)
            else:
                try:
                    values_list[i1][i2] = int(value)
                except: pass
    json_list = []
    for line in values_list:
        json_dict = {}
        for v_index, value in enumerate(line):
            json_dict.update({keys_list[v_index]: value})
        json_list += [json_dict]
    json_list = json.dumps(json_list, indent=4)
    print(json_list)
    with open(converted_file_path, 'w') as f:
        f.write(json_list)


converted_file_path = 'jsoned_csv.json'
file_path = "input.csv"
csv_into_jason(file_path, converted_file_path)