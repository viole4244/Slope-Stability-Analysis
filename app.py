import streamlit as st
import numpy as np
import pandas as pd
import pickle
pickle_in = open("Classifier.pkl", "rb")
model = pickle.load(pickle_in)
def welcome():
    return "Welcome All"
def ceml(density,cohesion,friction,angle,height,ppr):
    prediction = model.predict([[float(density), float(cohesion), float(friction), float(angle), float(height), float(ppr)]])
    print(prediction)
    return prediction


def main():
    st.title("Slope Stability analysis")
    html_temp = """
    <div style="background-color:Brown;padding:10px">
    <h2 style="color:Black;text-align:center;">Streamlit Slope Stability Predictor </h2>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)
    Density= st.text_input("Density", "Type Here")
    Cohesion = st.text_input("Cohesion", "Type Here")
    Friction = st.text_input("Friction", "Type Here")
    Angle= st.text_input("Angle", "Type Here")
    Height= st.text_input("Height", "Type Here")
    Ppr = st.text_input("Pore pressure ratio", "Type Here")
    result = ""
    if st.button("Predict"):
        result = ceml(Density,Cohesion,Friction,Angle,Height,Ppr)
    if result == 1:
       st.success('The Slope is Stable')
    elif result == 0:
        st.success('The Slope is not stable')
    if st.button("About"):
        st.text("Lets LEarn")
        st.text("Built with Streamlit")


if __name__ == '__main__':
    main()
