import json
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import (
    cosine_similarity,
    euclidean_distances,
)

with open('./texts.json', 'r') as f:
    data = json.load(f)

title_to_index = {title: i for i, title in enumerate(data.keys())}
index_to_title = {i: title for title, i in title_to_index.items()}
texts = list(data.values())

vectorizer = TfidfVectorizer()
sparse_vectors = vectorizer.fit_transform(texts)

# 文章の類似度
query = '借りぐらしのアリエッティ' # クエリとなるテキストのタイトル
# query = 'ルパン三世ｖｓ名探偵コナンＴＨＥＭＯＶＩＥ'
query_index = title_to_index[query]

sim = cosine_similarity(sparse_vectors[query_index], sparse_vectors)
sim[0][query_index] = -1 # 自身との類似度を0にする
most_similar_index = sim.argmax()
print('-' * 20)
print('query_title = ', texts[query_index].replace(' ', ''))
print('query_text = ', texts[query_index].replace(' ', ''))
print('-' * 20)
print('similarity = ', sim[0][most_similar_index])
print('similar_title = ', index_to_title[most_similar_index])
print('similar_text = ', texts[most_similar_index].replace(' ', ''))

# [疑問] なぜ類似していると判断されたのだろうか？
# - 重要な単語はどれ？
# - 重要でないと判断された単語は?
# - もっと似ていると判断されるべき映画はあるだろうか？
# - cosine_similarityをeuclidiean_similaritiesに変換してみよう。結果は？
# [解析ヒント]
# - 04_tfidf.pyの方法で重みの大きい共通する単語を探してみよう