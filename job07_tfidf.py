import pandas as pd
from sklearn.feature_extraction.text import  TfidfVectorizer
from scipy.io import  mmwrite, mmread
import pickle

df_reviews = pd.read_csv('./crawling_data/datasets/movie_review_2018_2022.csv')
df_reviews.info()
df_reviews.dropna(inplace=True)
Tfidf = TfidfVectorizer(sublinear_tf=True)
Tfidf_matrix = Tfidf.fit_transform(df_reviews['cleaned_sentences'])

with open('./models/tfidf.pickle','wb') as f:
    pickle.dump(Tfidf,f)

mmwrite('./models/Tfidf_movie_review.mtx', Tfidf_matrix)



