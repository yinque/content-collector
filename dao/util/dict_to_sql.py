def dict_to_create_sql(d: dict):
    """
    字典变为sql创建字段名文本
    :param d: eg：{'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}
    :return: eg： [' (key1, key2, key3) ', ' (?, ?, ?) ', (value1, value2, value3)]:[str,str,tuple]
    """
    result1 = ''
    result2 = ''
    result3 = []
    for key, value in d.items():
        result1 += f'{key}, '
        result2 += '?, '
        result3.append(value)
    result1 = result1.rstrip(', ')
    result2 = result2.rstrip(', ')

    result1 = f' ({result1}) '
    result2 = f' ({result2}) '
    result3 = tuple(result3)

    return [result1, result2, result3]


def dict_to_update_sql(d: dict):
    """
    字典变为sql更新字段名文本
    :param d: eg：{'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}
    :return: eg： [' key1=?, key2=?, key3=? ', ('value1', 'value2', 'value3')]:[str,tuple]
    """
    result1 = ''
    result2 = []
    for key, value in d.items():
        result1 += f'{key}=?, '
        result2.append(value)
    result1 = result1.rstrip(', ')

    result2 = tuple(result2)

    return [result1, result2]