import json
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import (
    cosine_similarity,
    euclidean_distances,
)

with open('./texts.json', 'r', encoding="utf-8") as f:
    # 映画のタイトル(文字列)->あらすじ(文字列)の辞書
    data = json.load(f)

# 映画のタイトル(文字列)の配列
titles = [title for title in data.keys()]
# 映画のタイトル->インデックスの辞書
title_to_index = {title: i for i, title in enumerate(titles)}
# 映画のあらすじ（文字列）の配列
texts = [text for text in data.values()]

# 映画のあらすじでモデルの学習
vectorizer = TfidfVectorizer()
sparse_vectors = vectorizer.fit_transform(texts)

# 文章の類似度
query = '借りぐらしのアリエッティ' # クエリとなるテキストのタイトル
query_index = title_to_index[query]

# 類似度の計算。内部では総当たりの計算（ループ）が回っている
sim = cosine_similarity(sparse_vectors[query_index], sparse_vectors)
sim[0][query_index] = -1 # 自身との類似度を0にする
most_similar_index = sim.argmax() # 最も類似している映画のインデックス

# 結果の表示
print('-' * 20)
print('query_index = ', query_index)
print('query_title = ', titles[query_index])
print('query_text = ', texts[query_index].replace(' ', ''))
print('-' * 20)
print('most_similar_index = ', most_similar_index)
print('similarity = ', sim[0][most_similar_index])
print('similar_title = ', titles[most_similar_index])
print('similar_text = ', texts[most_similar_index].replace(' ', ''))

# [疑問] なぜ類似していると判断されたのだろうか？
# - 重要な単語はどれ？
# - 重要でないと判断された単語は?
# - もっと似ていると判断されるべき映画はあるだろうか？
# - cosine_similarityをeuclidiean_similaritiesに変換してみよう。結果は？
# [解析ヒント]
# - 04_tfidf.pyの方法で重みの大きい共通する単語を探してみよう