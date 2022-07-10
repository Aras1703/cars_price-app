import pandas as pd
import numpy as np
import streamlit as st
import plotly.graph_objects as go
import pickle
from sklearn.preprocessing import LabelEncoder


def convert_categorical(df):
    column = ['Location', 'Fuel_Type', 'Transmission', 'Owner_Type', 'Mileage_measure',]

    for i, col in enumerate(column):
        encoder = LabelEncoder()
        encoder.classes_ = np.load(f'model/Model/label_encoder-{i}.npy', allow_pickle=True)
        df[col] = encoder.transform(df[col])

    return df
        

def convert_numeric(df):
    numerical = ['Location', 'Year', 'Kilometers_Driven', 'Fuel_Type', 'Transmission', 'Owner_Type', 'Seats',
            'Mileage_value', 'Mileage_measure', 'Engine_value', 'Power_value', 'is_after_2014',
            'is_kilometers_driven_less_80k', 'is_diesel', 'is_automatic', 'is_2_seats']
    
    scaler = pickle.load(open('model/Model/scaler.pkl', 'rb'))
    df[numerical] = scaler.transform(df[numerical].values)

    return df


def map_data(data, value):
    st.write("")
    st.write("")

    col1, = st.columns(1)

    with col1:
        st.write("#### **Inputed Data :**")

        df_show = [[value[k] for k in range(0, 16)]]
        df_show.insert(0, [
            'Location', 'Year', 'Kilometers_Driven', 'Fuel_Type', 'Transmission', 'Owner_Type', 'Seats',
            'Mileage_value', 'Mileage_measure', 'Engine_value', 'Power_value', 'is_after_2014',
            'is_kilometers_driven_less_80k', 'is_diesel', 'is_automatic', 'is_2_seats'])

        fig = go.Figure(data=[go.Table(
            columnwidth=200,
            header=dict(
                values=[['<b>Features</b>'],
                        ['<b>Input</b>']],
                line_color='darkslategray',
                fill_color='#ffffff',
                font=dict(color='blue', size=15),
                height=30
            ),
            cells=dict(
                values=df_show,
                line_color='darkslategray',
                fill=dict(color='blue'),
                height=30,
                font_size=15)
        )
        ])

        fig.update_layout(margin=dict(l=0, r=0, t=5, b=0), width=400, height=550)
        st.plotly_chart(fig)

    l_location = ['Ahmedabad', 'Bangalore', 'Chennai', 'Coimbatore',
                  'Delhi', 'Hyderabad', 'Jaipur', 'Kochi', 'Kolkata',
                  'Mumbai', 'Pune',]

    l_fuel_type = ['CNG', 'Diesel', 'Petrol', 'LPG', 'Electric',]
    l_transmission = ['Automatic', 'Manual',]
    l_owner_type = ['First', 'Second', 'Third', 'Fourth & Above',]
    l_mileage_measure = ['km/kg', 'kmpl',]

    data[0] = l_location[data[0]]
    data[3] = l_fuel_type[data[3]]
    data[4] = l_transmission[data[4]]
    data[5] = l_owner_type[data[5]]
    data[8] = l_mileage_measure[data[8]]

    df_train_raw = [data[k] for k in range(0, 16)]

    for i, val in enumerate(df_train_raw):
        if val == 'Yes':
            df_train_raw[i] = 1
        elif val == 'No':
            df_train_raw[i] = 0

    df_train = pd.DataFrame([df_train_raw], columns=[
            'Location', 'Year', 'Kilometers_Driven', 'Fuel_Type', 'Transmission', 'Owner_Type', 'Seats',
            'Mileage_value', 'Mileage_measure', 'Engine_value', 'Power_value', 'is_after_2014',
            'is_kilometers_driven_less_80k', 'is_diesel', 'is_automatic', 'is_2_seats'])

    df_train = convert_categorical(df_train)
    df_train = convert_numeric(df_train)

    #with col2:
    #    st.write("#### **Hasil Preprocessing :**")
    #    df_show_pre = df_train.iloc[[0]].values.tolist()
    #    df_show_pre.insert(0, [
    #        'Umur', 'Pekerjaan', 'Status', 'Edukasi', 'Kredit Default', 'Saldo Tahunan', 'Kredit Rumah',
    #        'Kredit Pribadi', 'Kontak', 'Hari', 'Bulan', 'Durasi', 'Kampanye', 'Terakhir Dikontak',
    #        'Kontak Sebelumnya', 'Hasil Kampanye'])

    #    fig = go.Figure(data=[go.Table(
    #        columnwidth=200,
    #        header=dict(
    #            values=[['<b>Kolom</b>'],
    #                    ['<b>Hasil Inputan</b>']],
    #            line_color='darkslategray',
    #            fill_color='#ff4a3d',
    #            font=dict(color='white', size=15),
    #            height=30
    #        ),
    #        cells=dict(
    #            values=df_show_pre,
    #            line_color='darkslategray',
    #            fill=dict(color='white'),
    #            height=30,
    #            font_size=15,
    #        ),
    #    )
    #    ])

    #    fig.update_layout(margin=dict(l=0, r=0, t=5, b=0), width=400, height=550)
    #    st.plotly_chart(fig)

    return df_train