# 辞書型はkey -> valueの関係を表す
dictionary = {
    'key1': 'value1',
    'key2': 'value2',
}

# 以下の行を差し込んで実行すると、その行で一時ストップする
import pdb; pdb.set_trace()

dictionary['new_key'] = 'new_value'

# どこでも差し込めます
for i in range(10):
    import pdb; pdb.set_trace()

# デバッガー起動時は
# `c`+Enterで続きを実行
# `変数名`+Enterでその変数を表示. i.e. `dict``
# `exit`+Enterで終了
