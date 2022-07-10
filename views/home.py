import streamlit as st
from model.preprocessing import map_data
from model.predict import predict_price


def app():
    st.write("## **Cars Price Prediction**")
    st.write("")

    st.write("#### **Input Data**")
    col1, col2, col3 = st.columns(3)

    with col1:
        year = st.number_input("Input Year :", min_value=1998, max_value=2019)

    with col2:
        km_driven = st.number_input('Input Kilometers Driven :',min_value=0, max_value=300000)

    with col3:
        opt_fuel_type = ['CNG', 'Diesel', 'Petrol', 'LPG', 'Electric']
        fuel_type = st.selectbox('Pick Fuel Type :', range(len(opt_fuel_type)),
                                  format_func=lambda x: opt_fuel_type[x])

    col4, col5, col6 = st.columns(3)

    with col4:
        opt_year_after_2k14 = ['Yes', 'No']
        year_after_2k14 = st.radio('Is the car above 2014 ?', range(len(opt_year_after_2k14)),
                                  format_func=lambda x: opt_year_after_2k14[x])

    with col5:
        opt_km_driven_less80k = ['Yes', 'No']
        km_driven_less80k = st.radio('Is the car km driven under 80k ?', range(len(opt_km_driven_less80k)),
                                  format_func=lambda x: opt_km_driven_less80k[x])

    with col6:
        opt_fuel_type_diesel = ['Yes', 'No']
        fuel_type_diesel = st.radio('Is the car fuel type diesel ?', range(len(opt_fuel_type_diesel)),
                                  format_func=lambda x: opt_fuel_type_diesel[x])

    col7, col8, col9 = st.columns(3)

    with col7:
        opt_loc = ['Mumbai', 'Hyderabad', 'Kochi', 'Coimbatore', 'Pune', 'Delhi', 'Kolkata', 'Chennai',
                   'Jaipur', 'Bangalore', 'Ahmedabad']
        location = st.selectbox('Pick Location :', range(len(opt_loc)), format_func=lambda x: opt_loc[x])

    with col8:
        opt_owner_type = ['First', 'Second', 'Third', 'Four or Above']
        owner_type = st.selectbox('Pick Owner Type :', range(len(opt_owner_type)), 
                                   format_func=lambda x: opt_owner_type[x])

    with col9:
        engine_value = st.number_input('Input Engine (CC) :', min_value=0, max_value=99999)

    col10, col11, col12 = st.columns(3)

    with col10:
        opt_transmission = ['Automatic', 'Manual']
        transmission = st.selectbox('Pick Transmission Type :', range(len(opt_transmission)), 
                                     format_func=lambda x: opt_transmission[x])
    with col11:
        seats = st.number_input(label='Input Seats :', min_value=2, max_value=10)

    with col12:
        power_value = st.number_input('Input Power (BHP) :', min_value=0.0, max_value=99999.0)

    col13, col14, col15 = st.columns(3)

    with col13:
        opt_transmission_automatic = ['Yes', 'No']
        transmission_automatic = st.radio('Is the transmission car automatic ?', range(len(opt_transmission_automatic)), 
                                     format_func=lambda x: opt_transmission_automatic[x])

    with col14:
        opt_seats2 = ['Yes', 'No']
        seats2 = st.radio('Is the car seats 2 ?', range(len(opt_seats2)), 
                                     format_func=lambda x: opt_seats2[x])
    
    with col15:
        pass

    col16, col17, col18 = st.columns(3)

    with col16:
        mileage_value = st.number_input('Input Mileage Car :', min_value=0.0, max_value=99999.0)

    with col17:
        opt_mileage_measure = ['km/kg', 'kmpl']
        mileage_measure = st.selectbox("Pick Mileage Measure :", range(len(opt_mileage_measure)),
                                        format_func=lambda x: opt_mileage_measure[x])

    with col18:
        pass

    col19, col20, col21 = st.columns(3)

    with col19:
        pass

    with col20:
        st.write("")
        st.write("")
        prediksi = st.button('Predict Price')
    
    with col21:
        st.write("")
        st.write("")
        st.write("")
        st.markdown('<p style="color:red;font-weight:500;text-align:center">All Data must be input !!! </p>', unsafe_allow_html=True)

    if prediksi:
        raw = [location, year, km_driven, fuel_type, transmission, owner_type, seats,
               mileage_value, mileage_measure, engine_value, power_value, year_after_2k14,
               km_driven_less80k, fuel_type_diesel, transmission_automatic, seats2,]
               
        value = [opt_loc[location], year, km_driven, opt_fuel_type[fuel_type], opt_transmission[transmission], 
                 opt_owner_type[owner_type], seats, mileage_value, opt_mileage_measure[mileage_measure], 
                 engine_value, power_value, opt_year_after_2k14[year_after_2k14],
                 opt_km_driven_less80k[km_driven_less80k], opt_fuel_type_diesel[fuel_type_diesel], 
                 opt_transmission_automatic[transmission_automatic], opt_seats2[seats2],]

        predict_price(map_data(raw, value))