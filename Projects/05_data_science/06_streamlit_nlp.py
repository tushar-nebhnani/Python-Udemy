import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import TfidfVectorizer
import streamlit as st

@st.cache_resource
def load_model():
    df = pd.read_csv("youtube_comments.csv")
    
    model = Pipeline([
        ('tfidf', TfidfVectorizer()),
        ('clf', LogisticRegression())
    ])

    model.fit(df['comment'], df['label'])
    return model 

model = load_model()
st.title("Youtube Comemnt Classifier!")
st.write("Classify your comment as toxic or supportive")
user_input = st.text_area("Enter a youtube comment: ")

if user_input:
    predict = model.predict([user_input])[0]
    if predict == "toxic":
        st.error("TOXIC COMMENT.")
    else:
        st.success("SUPPORTIVE COMMENT.")