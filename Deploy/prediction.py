import streamlit as st
import pandas as pd
import joblib
import datetime

def run():
    # Tampilan judul halaman
    st.markdown("<h1 style='text-align: center;'>Welcome to the Fraud Transaction Prediction Model</h1>", unsafe_allow_html=True)
    st.markdown("========================================================================================")
    
    st.title("Input Data Transaksi")

    def user_input():
        col1, col2 = st.columns(2)
        transaction_id = col1.number_input("Transaction ID", value=0)
        customer_id = col2.number_input("Customer ID", value=0)
        terminal_id = col1.number_input("Terminal ID", value=0)
        tx_amount = col2.number_input("Total Transaction", value=0.0)
        selected_hour = st.slider("Select Hour", 0, 23, 0)
        selected_minute = st.slider("Select Minute", 0, 59, 0)
        selected_second = st.slider("Select Second", 0, 59, 0)
        selected_date = st.date_input("Select Transaction Date", datetime.date.today())
        
        reference_date = datetime.datetime(2023, 1, 1, 0, 0, 0) 
        selected_datetime = datetime.datetime.combine(selected_date, datetime.time(selected_hour, selected_minute, selected_second))
        tx_time = selected_datetime - reference_date
        tx_time_seconds = int(tx_time.total_seconds())
        tx_time_days = tx_time.days
        
        data = {
            'TRANSACTION_ID': transaction_id,
            'CUSTOMER_ID' : customer_id,
            'TERMINAL_ID' : terminal_id,
            'TX_AMOUNT': tx_amount,
            'TX_TIME_SECONDS': tx_time_seconds,
            'TX_TIME_DAYS': tx_time_days
        }
        
        features = pd.DataFrame(data, index=[0])        
        return features

    # Menjalankan fungsi input pengguna
    input = user_input()

    # Menampilkan hasil input pengguna dalam bentuk tabel
    st.markdown("<h2 style='text-align: left;'>User Input Result</h2>", unsafe_allow_html=True)
    st.table(input)

    # Memuat model yang telah disimpan sebelumnya
    load_model = joblib.load("my_model.pkl")

    # Tombol untuk memprediksi
    if st.button("Predict", help='Click me!'):
        # Melakukan prediksi menggunakan model
        prediction = load_model.predict(input)

        # Menampilkan hasil prediksi
        if prediction == 1:
            prediction = 'Fraud Transaction'
        else:
            prediction = 'Normal Transaction'
  
        st.markdown("<h4 style='text-align: center;'>Berdasarkan informasi yang diberikan oleh pengguna, model Fraud Transaction memprediksi:</h4>", unsafe_allow_html=True)
        st.markdown(f"<h1 style='text-align: center;'>{prediction}</h1>", unsafe_allow_html=True)
        
        # Menampilkan hasil tambahan jika input termasuk dalam salah satu jenis fraud
        if prediction != "Normal Transaction":
            st.markdown("<h4 style='text-align: center;'>Transaksi ini termasuk dalam kategori mencurigakan. Harap waspada!</h4>", unsafe_allow_html=True)


