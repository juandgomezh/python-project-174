from gendiff.parser import load_json

def format_value(value):
    if value is None:
        return "null"
    if isinstance(value, bool):
        return str(value).lower()
    return str(value)

def generate_diff(file_path1: str, file_path2: str) -> str:
    data1 = load_json(file_path1)
    data2 = load_json(file_path2)
    
    dict_keys1 = data1.keys()
    dict_keys2 = data2.keys()
    
    keys = set(dict_keys1).union(dict_keys2)
    ordered_keys = sorted(keys)
    
    lst_diff = []
    
    for key in (ordered_keys):
        value1 = data1.get(key, None)
        value2 = data2.get(key, None)
        tmp = None
        if key in data1 and key not in data2:
            tmp = format_value(value1)
            lst_diff.append(f"  - {key}: {tmp}")
        elif key not in data1 and key in data2:
            tmp = format_value(value2)
            lst_diff.append(f"  + {key}: {tmp}")
        elif key in data1 and key in data2:
            if value1 != value2:
                tmp1 = format_value(value1)
                tmp2 = format_value(value2)
                lst_diff.append(f"  - {key}: {tmp1}")
                lst_diff.append(f"  + {key}: {tmp2}")
            else:
                tmp = format_value(value1)
                lst_diff.append(f"    {key}: {tmp}")
    return "{\n" + "\n".join(lst_diff) + "\n}"