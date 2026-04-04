# 辞書型はkey -> valueの関係を表す
dictionary = {
    'key1': 'value1',
    'key2': 'value2',
}

# keyに存在する文字列でアクセスできる
print('-------')
print(dictionary['key1'])
print(dictionary['key2'])
# print(dict['key3']) # 存在しないkeyはエラーとなる

# keyの追加
print('-------')
dictionary['new_key'] = 'new_value'
dictionary[1] = 'integer is fine'
print(dictionary)

# keyだけを配列として抽出
print('-------')
print([key for key in dictionary.keys()])

# valueだけを配列として抽出
print('-------')
print([value for value in dictionary.values()])