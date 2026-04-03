from janome.tokenizer import Tokenizer

tokenizer = Tokenizer()
tokenized_list = tokenizer.tokenize('地球は丸かった', wakati=True)
for token in tokenized_list:
    print(token)