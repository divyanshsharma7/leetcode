def merge_dicts(dict1, dict2):
    result = dict1.copy()  # Make a copy of the first dictionary
    for key, value in dict2.items():  
        result[key] = result.get(key, 0) + value  
    return result

dict1 = {'a': 10, 'b': 20}
dict2 = {'b': 5, 'c': 15}
merged_dict = merge_dicts(dict1, dict2)
print(merged_dict)
