import pickle
import streamlit as st
import numpy as np
import plotly.graph_objects as go

def predict(Location, Year,	Kilometers_Driven, Fuel_Type, Transmission,	Owner_Type,	Seats,
            Mileage_value, Mileage_measure, Engine_value, Power_value, is_after_2014,
            is_kilometers_driven_less_80k, is_diesel, is_automatic,	is_2_seats):
    dt = pickle.load(open('model/Model/decision_tree_model.pkl', 'rb'))
    knn = pickle.load(open('model/Model/knearest_neighbor_model.pkl', 'rb'))
    lr = pickle.load(open('model/Model/linear_regression_model.pkl', 'rb'))
    rf = pickle.load(open('model/Model/random_forest_model.pkl', 'rb'))
    svm = pickle.load(open('model/Model/support_vector_model.pkl', 'rb'))

    df = [[Location, Year,	Kilometers_Driven, Fuel_Type, Transmission, Owner_Type,	Seats,
           Mileage_value, Mileage_measure, Engine_value, Power_value, is_after_2014,
           is_kilometers_driven_less_80k, is_diesel, is_automatic, is_2_seats]]

    result_dt = dt.predict(df)
    result_knn = knn.predict(df)
    result_lr = lr.predict(df)
    result_rf = rf.predict(df)
    result_svm = svm.predict(df)

    return result_dt, result_knn, result_lr, result_rf, result_svm


def predict_price(Location, Year, Kilometers_Driven, Fuel_Type, Transmission, Owner_Type, Seats,
                  Mileage_value, Mileage_measure, Engine_value, Power_value, is_after_2014,
                  is_kilometers_driven_less_80k, is_diesel, is_automatic, is_2_seats):
    st.write("### **Hasil Prediksi Model**")
    dt, knn, lr, rf, svm, = predict(Location, Year,	Kilometers_Driven, Fuel_Type, Transmission,	Owner_Type,	Seats,
    	                           Mileage_value, Mileage_measure, Engine_value, Power_value, is_after_2014, 
                                   is_kilometers_driven_less_80k, is_diesel, is_automatic, is_2_seats)
    name = ['Decision Tree', 'K-Nearest Neighbor', 'Linear Regression', 'Random Forest', 'Support Vector Machine']
    results = [dt, knn, lr, rf, svm,]
    df_model = []
    df_pred = []

    for i, res in zip(name, results):
        df_model.append(i)
        df_pred.append(np.round(res,3))

    fig = go.Figure(data=[go.Table(
        header=dict(
            values=['Model', 'Prediksi'],
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