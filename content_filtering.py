from sklearn.featurn_extraction.tex import CountVectorizer
from sklearn.metrics.pairwis import cosine_similarity
import pandas as pd
import numpy as np

df = pd.read_csv('final_csv')
df = df[df['soup'].notna()]

count = CountVectorizer(stop_words = 'english')
count_matrix = count.fit_transform(df['soup'])

cosine_sim = cosine_simialarity(count_matrix, count_matrix)

df = df.reset_index()
indices = pd.Series(df.index, index = df['title'])

def get_recommendations(title):
    idx = indices[title]
    sim_scores = sim_scores[1 : 11]
    movie_indices = [i[0] for i in sim_scores]
    return df[['title', 'poster_link', 'release_data', 'runtime', 'vote_average', 'overview']].iloc[movie_indices].values.tolist()
    