import json
from janome.tokenizer import Tokenizer

with open('./train.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

texts = {
    datum['movie_title']: '\n'.join(datum['knowledge']['あらすじ'])
    for datum in data
}

# 分ち書きに変換
tokenizer = Tokenizer()
texts = {
     title: ' '.join(tokenizer.tokenize(text, wakati=True))
     for title, text in texts.items()
}

with open('./texts.json', 'w', encoding="utf-8") as f:
    json.dump(texts, f, indent=2, ensure_ascii=False)    