# Task 5-7

import json

if __name__ == '__main__':
    with open(r'text_7.txt', 'r', encoding='utf-8') as f:
        lines = [line.replace('\n', '') for line in f]
    print('Список строк: ', lines)

    result_list = []
    dict_corp = {}
    for line in lines:
        name, ownership, revenue_s, costs_s = line.split()
        revenue = int(revenue_s)
        costs = int(costs_s)
        earning = revenue - costs
        dict_corp[name] = earning

    dict_average = {}
    sum_earnings = 0
    num_positive = 0
    for earning in dict_corp.values():
        if earning > 0:
            num_positive += 1
            sum_earnings += earning
    dict_average['average_profit'] = float(sum_earnings) / float(num_positive)

    result_list.append(dict_corp)
    result_list.append(dict_average)
    print('Result list:', result_list)

    print('Do Serialize to file test-5-7.json')
    with open(r'test-5-7.json', 'w', encoding='utf-8') as f:
        json.dump(result_list, f, ensure_ascii=False, indent=4)

    print('Do Deserialize:')
    with open(r'test-5-7.json', 'r', encoding='utf-8') as f:
        result_json_obj = json.load(f)
    print('result_json_obj =  ', result_json_obj)
