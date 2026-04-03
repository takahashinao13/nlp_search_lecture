# 辞書型はkey -> valueの関係を表す
dictionary = {
    'key1': 'value1',
    'key2': 'value2',
}

# keyでアクセスできる
print('-------')
print(dictionary['key1'])
print(dictionary['key2'])
# print(dict['key3']) # 存在しないkeyはエラーとなる

# keyの追加もできる
dictionary['new_key'] = 'new_value'
print('-------')
print(dictionary)

# keyだけを配列として抽出
print('-------')
print([key for key in dictionary.keys()])

print('-------')
# valueだけを配列として抽出
print([value for value in dictionary.values()])