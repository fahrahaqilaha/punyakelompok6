import streamlit as st
import requests
import base64
import streamlit_lottie

def menu_biologi():
    st.subheader("Pemeriksaan Kualitas Air - Biologi")
    baku_mutu_biologi = {"Koliform": 50, "E. coli": 0}
    
    koliform = st.number_input("Masukkan jumlah Koliform (per 100ml): ", min_value=0, step=1)
    e_coli = st.number_input("Masukkan jumlah E. coli (per 100ml): ", min_value=0, step=1)
    
    if st.button("Periksa Biologi"):
        if koliform <= baku_mutu_biologi["Koliform"]:
            st.write("Koliform: Memenuhi baku mutu")
        else:
            st.write("Koliform: Tidak memenuhi baku mutu")
        
        if e_coli <= baku_mutu_biologi["E. coli"]:
            st.write("E. coli: Memenuhi baku mutu")
        else:
            st.write("E. coli: Tidak memenuhi baku mutu")

def menu_kimia():
    st.subheader("Pemeriksaan Kualitas Air - Kimia")
    baku_mutu_kimia = {"Kesadahan": 500, "Nitrat": 10, "Nitrit": 1, "Sulfat": 400, "Fluor": 1.5, "Besi": 1.0}
    
    kesadahan = st.number_input("Masukkan nilai Kesadahan (mg/L): ", min_value=0.0, step=0.1)
    nitrat = st.number_input("Masukkan nilai Nitrat (mg/L): ", min_value=0.0, step=0.1)
    nitrit = st.number_input("Masukkan nilai Nitrit (mg/L): ", min_value=0.0, step=0.1)
    sulfat = st.number_input("Masukkan nilai Sulfat (mg/L): ", min_value=0.0, step=0.1)
    fluor = st.number_input("Masukkan nilai Fluor (mg/L): ", min_value=0.0, step=0.1)
    besi = st.number_input("Masukkan nilai Besi (mg/L): ", min_value=0.0, step=0.1)
    
    if st.button("Periksa Kimia"):
        if kesadahan <= baku_mutu_kimia["Kesadahan"]:
            st.write("Kesadahan: Memenuhi baku mutu")
        else:
            st.write("Kesadahan: Tidak memenuhi baku mutu")
        
        if nitrat <= baku_mutu_kimia["Nitrat"]:
            st.write("Nitrat: Memenuhi baku mutu")
        else:
            st.write("Nitrat: Tidak memenuhi baku mutu")
        
        if nitrit <= baku_mutu_kimia["Nitrit"]:
            st.write("Nitrit: Memenuhi baku mutu")
        else:
            st.write("Nitrit: Tidak memenuhi baku mutu")
        
        if sulfat <= baku_mutu_kimia["Sulfat"]:
            st.write("Sulfat: Memenuhi baku mutu")
        else:
            st.write("Sulfat: Tidak memenuhi baku mutu")
        
        if fluor <= baku_mutu_kimia["Fluor"]:
            st.write("Fluor: Memenuhi baku mutu")
        else:
            st.write("Fluor: Tidak memenuhi baku mutu")
        
        if besi <= baku_mutu_kimia["Besi"]:
            st.write("Besi: Memenuhi baku mutu")
        else:
            st.write("Besi: Tidak memenuhi baku mutu")

def menu_fisika():
    st.subheader("Pemeriksaan Kualitas Air - Fisika")
    baku_mutu_fisika = {"Suhu": 40.0, "Rasa": "Tawar", "Bau": "Tidak berbau", "Warna": "Tidak berwarna", "TDS": 1000}
    
    suhu = st.number_input("Masukkan suhu air (°C): ", min_value=0.0, step=0.1)
    rasa = st.text_input("Masukkan rasa air: ")
    bau = st.text_input("Masukkan bau air: ")
    warna = st.text_input("Masukkan warna air: ")
    tds = st.number_input("Masukkan nilai TDS (mg/L): ", min_value=0.0, step=0.1)
    
    if st.button("Periksa Fisika"):
        if suhu <= baku_mutu_fisika["Suhu"]:
            st.write("Suhu: Memenuhi baku mutu")
        else:
            st.write("Suhu: Tidak memenuhi baku mutu")
        
        if rasa.lower() == baku_mutu_fisika["Rasa"].lower():
            st.write("Rasa: Memenuhi baku mutu")
        else:
            st.write("Rasa: Tidak memenuhi baku mutu")
        
        if bau.lower() == baku_mutu_fisika["Bau"].lower():
            st.write("Bau: Memenuhi baku mutu")
        else:
            st.write("Bau: Tidak memenuhi baku mutu")
        
        if warna.lower() == baku_mutu_fisika["Warna"].lower():
            st.write("Warna: Memenuhi baku mutu")
        else:
            st.write("Warna: Tidak memenuhi baku mutu")
        
        if tds <= baku_mutu_fisika["TDS"]:
            st.write("TDS: Memenuhi baku mutu")
        else:
            st.write("TDS: Tidak memenuhi baku mutu")

def menu_utama():
    st.title("Home")
    st.markdown(
        """
        Aplikasi ini digunakan untuk menentukan sample uji sesuai standar Buku Mutu Hygine Sanitasi,Peraturan Kementrian Kesehatan Republik Indonesia No 32 Tahun 2017.
      Tentang ndar Baku Mutu Kesehatan Lingkungan Dan Persyaratan Kesehatan Air Untuk Keperluan Higiene Sanitasi, Kolam Renang, Solus Per Aqua, Dan Pemandian Umum.

        Aplikasi ini untuk mempermudah dalam menyesuaikan nilai uji dengan parameter Fisika ,Biologi dan Kimia sesuai Baku Mutu Hygine Sanitasi.
        """
    )

def main():
    st.set_page_config(page_title="Pemeriksaan Kualitas Air", page_icon="home")

def main():
    
    menu = st.sidebar.selectbox("Pilih menu", ["Home", "Biologi", "Kimia", "Fisika", "Keluar"])
    st.sidebar.markdown("---")
    st.sidebar.header ("kelompok 6")

    if menu == "Home":
        menu_utama()
    elif menu == "Biologi":
        menu_biologi()
    elif menu == "Kimia":
        menu_kimia()
    elif menu == "Fisika":
        menu_fisika()
    elif menu == "Keluar":
        st.write("Terima kasih telah menggunakan aplikasi ini.")
        st.stop()

def img_to_base64(image_path):
    """Convert image to base64"""
    with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()
    
    # Import gambar & konversi ke base64
img_path = "imgs/icon_aka.png"  
img_base64 = img_to_base64(img_path)
st.sidebar.markdown(
    f'<img src="data:image/png;base64,{img_base64}" style="width: 100%; height: auto;">',
    unsafe_allow_html=True,
)

if __name__ == "__main__":
    main()

st.markdown("---")
st.markdown(
    """
    <style>
    .stApp {
        background-color: #90EE90;  /* Warna hijau muda */
    }
    </style>
    """,
    unsafe_allow_html=True
)
st.markdown("""
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css">
    <i class="fas fa-home"></i> 
""", unsafe_allow_html=True)

st.caption('<div style="text-align: center;">"Pengolahan Limbah Industri 2024"</div>', unsafe_allow_html=True)