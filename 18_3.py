import streamlit as st
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn import datasets


st.text("""
# Simple Iris flower prediction
""")

st.sidebar.header('User-input parameters')


def user_input_features():
    sepal_length = st.sidebar.slider('sepal_length', 0.0, 100.0, 2.2)
    sepal_width = st.sidebar.slider('sepal_width', 0.0, 100.0, 2.2)
    petal_length = st.sidebar.slider('petal_length', 0.0, 100.0, 2.2)
    petal_width = st.sidebar.slider('petal_width', 0.0, 100.0, 2.2)
    data = {
        'sepal_length': sepal_length,
        'sepal_width': sepal_width,
        'petal_length': petal_length,
        'petal_width': petal_width,
    }
    features = pd.DataFrame(data, index=[0])
    return features


df = user_input_features()

st.subheader('user input parameters')

st.write(df)

iris = datasets.load_iris()
X = iris.data
y = iris.target

clf = RandomForestClassifier()
clf.fit(X, y)

prediction = clf.predict(df)
prediction_proba = clf.predict_proba(df)

st.subheader('labels')
st.write(iris.target_names)

st.subheader('predictions')
st.write(iris.target_names[prediction])

st.subheader('pred probability')
st.write(prediction_proba)
