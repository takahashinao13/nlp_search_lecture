# 配列の扱い方について

# 数値も文字列も入れることができる
array = [1, 3, 4, 'name']

# 番号でアクセス
print('--------')
print(array[0])
print(array[1])

# リスト全体を表示する
print('--------')
print(array)

# 配列の中身を書き換える
print('--------')
array[0] = 'replaced'
print(array)