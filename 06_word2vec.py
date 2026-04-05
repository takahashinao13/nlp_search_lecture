import json
import gensim

with open('./texts.json', 'r', encoding="utf-8") as f:
    data = json.load(f)
# タイトル(文字列)の配列
texts = list(data.values())
texts = [text.split(' ') for text in texts]
# モデルの学習
model = gensim.models.Word2Vec(
    sentences=texts, sg=1,
    vector_size=100, window=3, min_count=5, workers=4,
    negative=10, epochs=100,
)

# 単語の一覧
print('vocab = ', model.wv.index_to_key)
# ベクトル化されていることを確認
word = 'アンディ'
index = model.wv.index_to_key.index(word)
print('word = ', word)
print('vector = ', model.wv.vectors[index])

# 他のインデックス（単語）のベクトルも確認してみよう