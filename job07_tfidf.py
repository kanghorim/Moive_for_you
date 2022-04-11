import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from scipy.io import mmwrite, mmread
import pickle

df_reviews = pd.read_csv('./crawling_data/datasets/movie_review_2018_2022.csv')
df_reviews.dropna(inplace=True)
df_reviews.to_csv('./crawling_data/datasets/movie_review_2018_2022.csv',
                  index=False)
df_reviews.info()

Tfidf = TfidfVectorizer(sublinear_tf=True)
Tfidf_matrix = Tfidf.fit_transform(df_reviews['cleaned_sentences'])

with open('./models/tfidf01.pickle', 'wb') as f:
    pickle.dump(Tfidf, f)
mmwrite('./models/Tfidf_movie_review01.mtx', Tfidf_matrix)
print('end')