"""
    Full of error debug soon.
"""

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer 
from sklearn.metrics.pairwise import cosine_similarity
import streamlit as st

df = pd.read_csv("books.csv")

vectorizer = TfidfVectorizer(stop_words='english')
tfidf_matrix = vectorizer.fit_transform(df['description'])

consine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

indeces = pd.Series(df.index, index=df['title'])

def get_recommendations(title, cosine_sim=consine_sim):
    idx = indeces[title]
    sim_scores = list(enumerate(consine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)[1:6]
    book_indices = [i[0] for i in sim_scores]
    return df[['title', 'author']].iloc[book_indices]

st.title("Book Recomendation Engine")
st.write("Enter a book title and get similar recommendation")

select_book = st.text_input("Book: ")

if select_book:
    results = get_recommendations(select_book, df, consine_sim, indeces)

    st.table(results)