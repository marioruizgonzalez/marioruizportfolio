import streamlit as st
import xgboost as xgb
import pandas as pd

#Loading up the Regression model we created
model = xgb.XGBRegressor()


def app():
    st.title('Model')

    st.write('This is the `Model` page of the multi-page app.')

    st.write('The model performance of the Iris dataset is presented below.')


    