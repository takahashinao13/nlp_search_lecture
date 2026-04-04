# 演習用資料


## 演習
- 01_tokenize.py: トークナイズの方法
- 02_show_noun.py: 名詞でのフィルタリング
- 03_preprocess.py: コーパスの前処理. 事前にコーパスをダウンロードする必要有
  https://github.com/ku-nlp/JMRD より./data/train.jsonを./train.jsonに保存する
  ```
  $ ls
  03_preprocess.py
  train.json
  ```
- 04_tfidf.py: tfidfでのベクトル化
- 05_naive_search.py: tfidfを利用した総当たり検索
- 06_word2vec.py: word2vecによる単語のベクトル化
- 07_similar_words.py: word2vecによる類似単語の検索

## 付録
- appendix_debugger.py: デバッガの使い方
- appendix_dict.py: 辞書の使い方
- appendix_list.py: 配列の使い方

## 引用元
本レポジトリは京都大学のJapanese Movie Recomendation Datasetを利用しております。素晴らしいデータをありがとうございます。
- データ: https://github.com/ku-nlp/JMRD/tree/main
