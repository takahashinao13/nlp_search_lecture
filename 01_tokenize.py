from janome.tokenizer import Tokenizer

tokenizer = Tokenizer()
tokenized_list = tokenizer.tokenize('地球は丸かった', wakati=True)
for token in tokenized_list:
    print(token)

# 他の文章でも試してみよう. 例: 'すもももももももものうち'
# wakati=Falseにしてみよう。品詞や読みなども取れる
# 英語はどうなるだろうか