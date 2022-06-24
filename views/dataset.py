import streamlit as sl
import pandas as pd

def app():
    sl.write("### **Dataset Train**")
    df_train = pd.read_csv('dataset/train-data.csv', sep=';')
    sl.write(df_train)

    sl.write("")

    sl.write("### **Dataset Test**")
    df_test = pd.read_csv('Dataset/test-data.csv', sep=';')
    sl.write(df_test)

    sl.write("")