import json
from sklearn.feature_extraction.text import TfidfVectorizer

with open('./texts.json', 'r', encoding="utf-8") as f:
    data = json.load(f)

# タイトル(文字列)の配列
texts = list(data.values())

# tfidfモデルの学習
vectorizer = TfidfVectorizer()
vectorizer.fit(texts)

# 単語配列の取得
words = vectorizer.get_feature_names_out()

# ベクトル化の確認
title = '時をかける少女'
text = data[title]
print('-------')
vector = vectorizer.transform([text])[0] # あらすじのベクトル化
for word_index, weight in enumerate(vector.toarray()[0]):
    if weight > 0: # 重要度weightが0以上のものだけ表示する
        print('\t', words[word_index], weight)

# indexを変えて他の映画の単語とその重みを確認してみよう
# 重要だと判断された単語はあなたの感覚と一致しますか？