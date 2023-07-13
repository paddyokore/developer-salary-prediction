import streamlit as sl
from predict_page import show_predict_page
from explore_page import show_explore_page
import warnings
warnings.filterwarnings('ignore')

page = sl.sidebar.selectbox("Predict or Explore", ("Predict", "Explore"))

if page == "Predict":
    show_predict_page()
else:
    show_explore_page()