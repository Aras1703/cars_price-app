import pickle
import streamlit as st
import numpy as np
import plotly.graph_objects as go


def predict(df):
    dt = pickle.load(open('model/Model/decision_tree_model.pkl', 'rb'))
    rf = pickle.load(open('model/Model/random_forest_model.pkl', 'rb'))

    result_dt = dt.predict(df)
    result_rf = rf.predict(df)

    return result_dt, result_rf, 

def predict_price(df):
    st.write("### **Result Prediction Model**")
    
    dt, rf, = predict(df)
    name = ['Decision Tree', 'Random Forest', ]
    results = [dt, rf,]
    df_model = []
    df_pred = []

    for mod, res in zip(name, results):
        df_model.append(mod)
        df_pred.append(np.round(res, 2))
    
    fig = go.Figure(data=[go.Table(
        header=dict(
            values=['Models', 'Prediction'],
            line_color='darkslategray',
            fill_color='#ffffff',
            font=dict(color='blue', size=15),
            height=30,
        ),
        cells=dict(
            values=[df_model, df_pred],
            line_color='darkslategray',
            fill=dict(color='blue'),
            font_size=15,
            height=30,
        ))
    ])

    fig.update_layout(margin=dict(l=0, r=0, t=5, b=0), width=550, height=550)
    st.plotly_chart(fig)