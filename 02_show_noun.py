from janome.tokenizer import Tokenizer

tokenizer = Tokenizer()
tokenized_list = tokenizer.tokenize('地球は丸かった', wakati=False)
for token in tokenized_list:
    if '名詞' in token.extra[0]:
        print(token.node.surface)