import json
from sklearn.feature_extraction.text import TfidfVectorizer

with open('./texts.json', 'r', encoding="utf-8") as f:
    data = json.load(f)

# タイトル(文字列)の配列
texts = list(data.values())

# tfidfモデルの学習とテキストの変換
vectorizer = TfidfVectorizer()
sparse_vectors = vectorizer.fit_transform(texts)

# 単語配列の取得
words = vectorizer.get_feature_names_out()

# index = 11の情報を確認する
index = 11
print('-------')
print(texts[index])
for word_index, weight in enumerate(sparse_vectors[index].toarray()[0]):
    if weight > 0: # 重要度weightが0以上のものだけ表示する
        print('\t', words[word_index], weight)

# indexを変えて他の映画の単語とその重みを確認してみよう
# 重要だと判断された単語はあなたの感覚と一致しますか？