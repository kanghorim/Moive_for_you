import pandas as pd
from konlpy.tag import Okt
import re

df = pd.read_csv('./crawling_data/cleaned_review_2018_20_50.csv')
print(df.head())
df.info()

okt = Okt()
count = 0
cleaned_sentences = []
for sentence in df.cleaned_sentences:
    count += 1
    if count % 10 ==0:
        print('.', end='')
    if count % 100 == 0:
        print()
    token = okt.pos(sentence, stem=True) # 품사 명사나 동사나 이런거 다 분류해줌
    # print(token)
    df_token = pd.DataFrame(token,  columns=['word', 'class'])
    df_token = df_token[(df_token['class']=='Noun') |
                                (df_token['class']=='Verb') |
                                (df_token['class']=='Adjective')]
    cleaned_sentence = ' '.join(df_token.word)
    # print(cleaned_sentence)
    cleaned_sentences.append(cleaned_sentence) # 다시 한문장으로 만들기
df['cleaned_sentences'] = cleaned_sentences
print(df.head())
df.info()
df.to_csv('./crawling_data/cleaned_review_2018_20_50_final.csv',
          index=False)