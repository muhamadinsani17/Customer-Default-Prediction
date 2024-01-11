# Import library yang digunakan
import streamlit as st
from PIL import Image

# Fungsi untuk menjalankan aplikasi
def run():
    
    # Tampilan judul halaman
    st.markdown("<h1 style='text-align: center;'>Welcome to Explaration Data Analysis</h1>", unsafe_allow_html=True)
    st.markdown("========================================================================================")
    st.markdown("")
    
    # Membagi layar menjadi dua kolom
    col1, col2 = st.columns(2)

    # Menampilkan visualisasi dan penjelasan untuk Default Payment Next Month by Education Level
    col1.markdown("<h4 style='text-align: left;'>1. Tinjauan Rata-Rata Fitur: Perbandingan Antara Transaksi Fraud dan Non-Fraud</h4>", unsafe_allow_html=True)
    image = Image.open('output1.png')
    col1.image(image, caption='figure 1')

    with col1.expander('Penjelasan'):
        st.caption('Berdasarkan Visulisasi diatas, hasil analisis dataset menunjukkan bahwa transaksi fraud cenderung melibatkan pelanggan dengan nilai CUSTOMER_ID lebih tinggi dan jumlah transaksi (TX_AMOUNT) yang signifikan. Namun, tidak ada pola yang jelas terkait waktu transaksi atau urutan transaksi. Deteksi fraud lebih terkait dengan nilai transaksi tinggi dan karakteristik pelanggan daripada faktor waktu.')

    # Menampilkan visualisasi dan penjelasan untuk Default Payment Next Month by Marital Status
    col2.markdown("<h4 style='text-align: left;'>2. Pemahaman Distribusi Fitur pada Transaksi Fraud: Boxplot Analysis</h4>", unsafe_allow_html=True)
    image = Image.open('output2.png')
    col2.image(image, caption='figure 2')

    with col2.expander('Penjelasan'):
        st.caption('- Transaksi non-fraud memiliki variasi yang cukup signifikan dalam jumlah, waktu, dan identifikasi pelanggan serta terminal. Tidak ada pola khusus atau kelompok pelanggan tertentu yang dapat diidentifikasi sebagai indikator transaksi non-fraud')
        st.caption('- Transaksi fraud menunjukkan variasi yang signifikan dalam jumlah, waktu, dan identifikasi pelanggan. Jumlah transaksi fraud cenderung jauh lebih tinggi daripada transaksi normal. Tetapi tidak ada pola yang jelas dalam identifikasi terminal yang dapat diidentifikasi untuk transaksi fraud.')

    # Menampilkan visualisasi dan penjelasan untuk Default Payment Next Month by Pay Status
    col1.markdown("<h4 style='text-align: left;'>3. Perbandingan Trend Jumlah Transaksi Fraud dan Non-Fraud per Hari: Lineplot Analysis</h4>", unsafe_allow_html=True)
    image = Image.open('output3.png')
    col1.image(image, caption='figure 3')

    with col1.expander('Penjelasan'):
        st.caption('Berdasarkan visualisasi transaksi per hari Subset data untuk transaksi fraud (warna biru) dan non-fraud (warna hijau) menunjukkan bahwa tidak terlihat pola yang konsisten atau jelas antara kedua kelas (fraud dan non-fraud) terkait fitur waktu (TX_TIME_DAYS). Dengan kata lain, tidak ada tren atau perubahan yang mencolok dalam distribusi jumlah transaksi per hari yang membedakan transaksi fraud dan non-fraud.')

    # Menampilkan visualisasi dan penjelasan untuk Default Payment Next Month by Bill Amount
    col2.markdown("<h4 style='text-align: left;'>4. Perbandingan Trend Jumlah Total Transaksi Fraud dan Non-Fraud per Hari: Lineplot Analysis</h4>", unsafe_allow_html=True)
    image = Image.open('output4.png')
    col2.image(image, caption='figure 4')

    with col2.expander('Penjelasan'):
        st.caption('Berdasarkan total jumlah transaksi per hari,Subset data untuk transaksi fraud (warna biru) dan non-fraud (warna hijau) tidak tampak adanya pola yang konsisten atau jelas yang membedakan antara transaksi fraud dan non-fraud. Dengan kata lain, tidak terdapat tren atau perubahan yang mencolok dalam distribusi total jumlah transaksi per hari yang memisahkan transaksi fraud dan non-fraud.')

    # Menampilkan visualisasi dan penjelasan untuk Default Payment Next Month by Age Range
    col1.markdown("<h4 style='text-align: left;'>5. Distribusi Transaksi Per Jam</h4>", unsafe_allow_html=True)
    image = Image.open('output5.png')
    col1.image(image, caption='figure 5')

    with col1.expander('Penjelasan'):
        st.caption('Dari visualisasi diatas, Subset data untuk transaksi fraud (warna merah) dan non-fraud (warna hijau) dapat disimpulkan bahwa distribusi transaksi pada jam-jam tertentu dalam sehari menunjukkan pola yang sesuai dengan harapan, dengan lonceng Gaussian yang baik untuk kedua kelas. Meskipun ada pola umum seperti puncak transaksi pada jam 1 siang, tidak terlihat pola yang jelas yang dapat membedakan antara transaksi fraud dan non-fraud.')

