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

# 類似した単語を探そう
query_word = 'アンディ'
print('word = ', query_word)
print(model.wv.most_similar(query_word))

# 他の単語でも試してみよう
# なぜ類似していると判断されたのだろうか？->元のテキストでの使われ方をみてみよう
# 元の文書にある単語がモデルに存在しない。どこで省かれたのだろうか？(分ち書き？word2vecのmin_count?)
# (難しい)文書ベクトルを作成して類似文書の検索をしてみよう
#   文章ベクトル = 単語ベクトルの重み付平均
#   重み -> tfidf