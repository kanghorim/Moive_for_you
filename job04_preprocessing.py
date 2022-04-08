import pandas as pd
from konlpy.tag import Okt
import re

df = pd.read_csv('./crawling_data/movie_review_onesentence_2018_20_50p.csv')
print(df.head())
df.info()

stopwords = pd.read_csv('./crawling_data/stopwords.csv')
stopwords_list = list(stopwords['stopword'])
cleaned_sentences = []
for review in df.reviews:
    review = re.sub('[^가-힣 ]', '', review)
    review_word = review.split(' ')

    words = []
    for word in review_word:
        if len(word) > 1:
            if word not in stopwords_list:
                words.append(word)
    cleaned_sentence = ' '.join(words)
    cleaned_sentences.append(cleaned_sentence)
df['cleaned_sentences'] = cleaned_sentences
df = df[['titles', 'cleaned_sentences']]
df.to_csv('./crawling_data/cleaned_review_2018_20_50.csv',
          index=False)
df.info()