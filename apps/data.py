import streamlit as st
import numpy as np
import pandas as pd
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report

def app():
    st.title('Data')

    st.write("This is the `Data` page of the multi-page app.")

    st.write("The following is the DataFrame of the `iris` dataset.")
    uploaded_file = st.file_uploader('test.csv')
    iris = datasets.load_iris()
    
    X = pd.DataFrame(iris.data, columns = iris.feature_names)
    Y = pd.Series(iris.target, name = 'class')
    df = pd.concat([X,Y], axis=1)
    df['class'] = df['class'].map({0:"setosa", 1:"versicolor", 2:"virginica"})

    st.write(df)
    
    # Load iris dataset
    iris = datasets.load_iris()
    X = iris.data
    Y = iris.target

    # Model building
    st.header('Model performance')
    X_train, X_test, Y_train, Y_test = train_test_split(
        X, Y, test_size=0.2, random_state=42)
    clf = RandomForestClassifier()
    clf.fit(X_train, Y_train)
    score = clf.score(X_test, Y_test)
    st.write('Accuracy:')
    st.write(score)