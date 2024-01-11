import streamlit as st
import eda
import prediction

# Membuat sidebar dengan opsi menu
page = st.sidebar.selectbox(label='Select Page:', options=['Home Page', 'Exploration Data Analysis', 'Model Prediction'])
st.sidebar.write('')
st.sidebar.write('')
st.sidebar.write('')
st.sidebar.write('')
st.sidebar.write('')
st.sidebar.image('https://cdn1.iconfinder.com/data/icons/online-money-service-aesthetics-vol-1/256/Fraud_alert-512.png')

# Memilih halaman berdasarkan opsi yang dipilih
if page == 'Home Page':
    # Tampilan Home Page
    st.image('https://149695847.v2.pressablecdn.com/wp-content/uploads/2018/02/splunkf1frauddetection-770x385.png')
    st.markdown("<h1 style='text-align: center;'>Welcome to Home Page<br>Milestone 2</h1>", unsafe_allow_html=True)
    st.markdown("========================================================================================")
    st.write('')
    st.markdown("<p style='text-align: left;'>Nama : Muhammad Insani</p>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: left;'>Batch : HCK-010</p>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: left;'>Objective : Program ini dibuat untuk memprediksi transaksi penipuan dari dataset yang terdiri dari 1,75 juta transaksi dengan menggunakan model terbaik diantara SVM, KNN, DecisionTree, Random Forest, dan Boosting</p>", unsafe_allow_html=True)
    st.write('')
    st.caption('Silahkan pilih menu lain di Select Box pada sebelah kiri layar anda untuk memulai!')
    st.write('')
    st.write('')



    # Menampilkan Deskripsi dataset
    with st.expander("Deskripsi Dataset"):
        st.caption('''
                   
                   Dataset ini terdiri dari 1,75 juta transaksi yang dilakukan dengan mempertimbangkan pengguna simulasi melalui berbagai terminal selama periode Januari 2023 hingga Juni 2023. Namun, data tersebut sangat tidak seimbang, dengan hanya sebagian kecil (13,45%) transaksi yang diklasifikasikan sebagai penipuan
                   
                   
                    | Kolom                | Deskripsi                                            |
                    |----------------------|--------------------------------------------------------|
                    | Unnamed: 0           | Indeks unik untuk setiap baris dalam dataset          |
                    | TRANSACTION_ID       | Pengidentifikasi unik untuk setiap transaksi           |
                    | TX_DATETIME          | Tanggal dan waktu transaksi                             |
                    | CUSTOMER_ID          | Pengidentifikasi unik untuk pelanggan yang melakukan transaksi |
                    | TERMINAL_ID          | Pengidentifikasi untuk terminal ATM atau POS tempat transaksi dilakukan |
                    | TX_AMOUNT            | Jumlah transaksi                                       |
                    | TX_TIME_SECONDS      | Waktu transaksi dalam detik sejak tengah malam         |
                    | TX_TIME_DAYS         | Waktu transaksi dalam hari sejak transaksi pertama dalam dataset |
                    | TX_FRAUD             | Label biner yang menunjukkan apakah transaksi tersebut merupakan transaksi fraud (1) atau bukan fraud (0) |
                    | TX_FRAUD_SCENARIO    | Label kategoris yang menunjukkan jenis transaksi fraud (misalnya, "pembelian dengan kartu curian" atau "pengambilalihan akun") |

                   
                   
                   ''')

    # Menampilkan latar belakang
    with st.expander("Latar Belakang"):
        st.caption('''
                   Di tengah revolusi digital dan pertumbuhan eksponensial transaksi keuangan global, perlindungan terhadap keamanan sistem pembayaran menjadi krusial. 
                   Dataset transaksi finansial global yang mencakup 1,75 juta kasus dari Januari hingga Juni 2023 memberikan peluang unik untuk mengeksplorasi dinamika 
                   penipuan di tingkat global. Namun, ketidakseimbangan distribusi data, dengan hanya 13,45% transaksi yang diidentifikasi sebagai penipuan, menciptakan 
                   tantangan nyata dalam pengembangan model prediktif yang dapat mengantisipasi dan menanggulangi pola penipuan yang semakin berkembang. Dalam konteks global ini, 
                   penelitian ini bukan hanya sekadar respons terhadap tren kecurangan terkini, tetapi juga sebuah langkah signifikan menuju penguatan keamanan dalam ekosistem 
                   transaksi keuangan yang semakin kompleks.
                   
                   ''')
        
    # Menampilkan problem statement
    with st.expander("Problem Statement"):
        st.caption('''
                   Dalam menghadapi ketidakseimbangan data transaksi keuangan, tantangan utamanya adalah memperbaiki model prediktif agar lebih cerdas dalam mengidentifikasi 
                   fraud transaction dengan label "TX_FRAUD". Fokusnya adalah mengurangi prediksi yang salah terhadap fraud, mengintegrasikan metrik evaluasi yang lebih cerdas 
                   daripada akurasi umum. Proyek ini bertujuan memberikan solusi cerdas dan efisien untuk meningkatkan keamanan sistem pembayaran dengan prediksi yang optimal 
                   terkait transaksi fraud. 
                   
                   ''')

    # Menampilkan Kesimpulan berdasarkan pemilihan model :
    with st.expander("Kesimpulan Berdasarkan Pemilihan Model"):
        st.caption('''
                   
                    Diantara model yang digunakan seperti SVM, KNN, Decision Tree, Random Forest, dan Boosting, Model Decision Tree mendemonstrasikan recall yang tinggi berdasarkan beberapa keunggulan tertentu:

                    - Memahami Pola Data:
                    Decision Tree secara alami mampu memahami dan mengekstraksi pola serta hubungan dalam data dengan efektif.

                    - Interpretabilitas yang Tinggi:
                    Struktur pohon keputusan memungkinkan interpretasi yang mudah oleh manusia, memudahkan pemahaman faktor-faktor yang berkontribusi pada prediksi fraud.

                    - Kemampuan Menangani Fitur Kategorikal:
                    Model ini dapat menangani baik fitur numerik maupun kategorikal tanpa transformasi tambahan, menjadi bermanfaat pada dataset dengan campuran jenis fitur.

                    - Menangani Pemisahan yang Non-linear:
                    Decision Tree dapat menangani pemisahan kelas yang non-linear, cocok untuk hubungan fitur dan label yang bersifat kompleks.

                    - Pengaturan Hyperparameter yang Mudah:
                    Melalui hyperparameter tuning, kinerja Decision Tree dapat dioptimalkan dengan penyesuaian kriteria split, kedalaman maksimum, dan jumlah sampel minimum.

                    - Kemampuan Menangani Imbalanced Data:
                    Model ini menunjukkan kinerja baik pada dataset yang tidak seimbang, seperti pada kasus deteksi fraud.

                    - Tingkat Kerumitan yang Sesuai:
                    Decision Tree memiliki tingkat kerumitan yang dapat disesuaikan, memungkinkan penyesuaian untuk mencapai keseimbangan antara underfitting dan overfitting.

                    Walaupun Decision Tree memiliki keunggulan ini, perlu diingat bahwa hasil tergantung pada karakteristik khusus dari dataset, dan dalam beberapa kasus, model lain mungkin lebih optimal.        
                                    
                                    
                   ''')


    # Menampilkan kesimpulan terhadap hasil model yang dipilih
    with st.expander("Kesimpulan Terhadap Hasil Model Yang Dipilih"):
        st.caption('''
                   
                   *1. Performa Umum Model:*

                    - Model ini memiliki hasil yang umumnya baik untuk kelas minoritas (1), model memiliki tingkat presisi sebesar 0.96, recall sebesar 0.98, dan F1-score sebesar 0.97 pada data uji.
                    - Tingkat True Positives dan True Negatives yang tinggi menunjukkan kemampuan model dalam mengidentifikasi transaksi fraud dan non-fraud dengan baik.

                    *2. Kesalahan Model:*

                    - Terdapat beberapa kasus False Negatives yang menunjukkan bahwa model masih melewatkan beberapa transaksi fraud. Ini dapat menjadi area perbaikan untuk meningkatkan recall pada kelas fraud.

                    *3. Karakteristik False Negatives:*

                    - Transaksi ini menunjukkan variasi nilai fitur, pola waktu yang tidak konsisten, dan kesalahan dalam mendeteksi fraud, menekankan perlunya peningkatan pada model untuk fokus pada pola khusus dan mengurangi jumlah kasus yang terlewat.

                    *4. Karakteristik True Negatives:*

                    - Transaksi yang berhasil diidentifikasi sebagai non-fraud (True Negatives) memiliki variasi nilai fitur yang wajar dan model berhasil memprediksinya dengan benar.

                    *5. Perbaikan Model:*

                    - Model dapat diperbaiki dengan meningkatkan analisis terhadap kasus-kasus False Negatives, mungkin dengan menambahkan fitur atau menyesuaikan parameter model.
                    - Fokus pada peningkatan recall untuk kelas fraud dapat membantu mengurangi jumlah False Negatives.

                    *6. Penggunaan Model:*

                    - Model ini dapat digunakan untuk deteksi fraud pada transaksi keuangan dengan tingkat akurasi yang tinggi. 
                    - Model dapat memberikan nilai tambah dalam memitigasi risiko fraud dan melindungi keuangan perusahaan.

                    *7. Pemantauan dan Peningkatan Lanjutan:*

                    - Model perlu dipantau secara berkala, dan perbaikan atau penyesuaian lanjutan diperlukan untuk menjaga kinerja model seiring waktu.
                    - Model ini dapat digunakan sebagai alat bantu dalam pengambilan keputusan terkait dengan deteksi fraud, namun perlu pemahaman kontekstual dan pemantauan yang berkelanjutan.
                   
                   
                   
                   
                   ''') 
        
    # Menampilkan kesimpulan terhadap problem statement 
    with st.expander("Kesimpulan Terhadap Problem Statement"):
        st.caption('''
                   
                   Dari pernyataan masalah, dapat disimpulkan bahwa model yang berhasil dikembangkan telah mencapai tingkat akurasi yang tinggi dalam mengenali transaksi fraud. Meskipun demikian, 
                   menghadapi ketidakseimbangan data menjadi tantangan, sehingga diperlukan fokus khusus untuk mengurangi kesalahan prediksi terhadap transaksi fraud. Penilaian model tidak hanya 
                   mengandalkan akurasi umum, tetapi juga mempertimbangkan metrik evaluasi yang lebih cerdas. Secara keseluruhan, model ini memberikan solusi yang cerdas dan efisien untuk meningkatkan 
                   keamanan sistem pembayaran dengan prediksi optimal terkait transaksi fraud. Meski demikian, masih terdapat peluang untuk perbaikan, terutama dalam mengatasi kasus False Negatives
                   
                   ''')
        
elif page == 'Exploration Data Analysis':
    # Menjalankan fungsi untuk EDA
    eda.run()
else:
    # Menjalankan fungsi untuk Model Prediction
    prediction.run()
