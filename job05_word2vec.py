from gensim.models import Word2Vec
import pandas as pd

review_word = pd.read_csv('crawling_data/datasets/moive_review_2018_2022.csv')
review_word.info()

cleaned_token_review = list(review_word['cleaned_sentences'])
print(cleaned_token_review[0])
cleaned_tokens = []
for sentence in cleaned_token_review:
    token = sentence.split()
    cleaned_tokens.append(token)
print(cleaned_tokens[0])

embedding_model = Word2Vec(cleaned_tokens, vector_size = 100, window = 4, min_count = 20,
                           workers = 4, epochs = 100, sg = 1)

embedding_model.save('./models/word2vecModel.model')
print(embedding_model.wv.vocab.key())
print(len(embedding_model.wv.vocab.key()))

