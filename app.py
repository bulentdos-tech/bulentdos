import streamlit as st
import pandas as pd
import os

# 1. AYARLAR
st.set_page_config(page_title="Prof. Dr. Bülent DÖŞ", layout="wide")

# 2. ÜST GÖRSEL
st.image("https://www.gantep.edu.tr/manset/manset_resim/47941_GAUN_3.jpg", use_container_width=True)

# 3. PROFİL VE ÖZGEÇMİŞ
col1, col2 = st.columns([1, 2.5])

with col1:
    try:
        st.image("profil.jpg", width=250)
    except:
        st.image("https://via.placeholder.com/250x300.png?text=Prof.+Dr.+Bulent+Dos", width=250)
    
    st.link_button("🔴 Google Scholar", "https://scholar.google.com/citations?user=xpLZ0O8AAAAJ", use_container_width=True)
    st.link_button("🔵 LinkedIn", "https://www.linkedin.com/in/b%C3%BClent-d%C3%B6%C5%9F-2018a017/", use_container_width=True)
    st.link_button("📸 Instagram", "https://www.instagram.com/bulenttdos/", use_container_width=True)
    st.info("📧 bulentdos@yahoo.com")

with col2:
    st.title("Prof. Dr. Bülent DÖŞ")
    st.subheader("Gaziantep Üniversitesi | Eğitim Bilimleri Fakültesi")
    
    # ÖZGEÇMİŞ METNİ (GÜVENLİ FORMAT)
    ozgecmis = (
        "Prof. Dr. Bülent Döş, Gaziantep Üniversitesi Eğitim Fakültesi’nde görev yapan deneyimli bir akademisyendir; "
        "öğretim programı geliştirme, öğretmen eğitimi, yükseköğretim ve eğitim teknolojileri gibi alanlarda odaklanan çalışmalarıyla tanınır. "
        "Google Scholar verilerine göre toplamda yaklaşık 970 atıf almış; bu atıflar onun çalışmalarının eğitim bilimleri literatüründe geniş bir etki yarattığını göstermektedir.\n\n"
        "Ayrıca profilinde yer alan yayınlar arasındaki etki ve üretkenlik ölçütlerine göre bilimsel üretimi düzenli şekilde atıf bulmaktadır; "
        "bu göstergeler, akademik çabalarının ulusal ve uluslararası alanda fark edildiğini ortaya koymaktadır. "
        "Prof. Dr. Döş, lisans ve lisansüstü düzeyde dersler vermekte, çok sayıda yüksek lisans ve doktora tezine başarıyla danışmanlık yapmakta "
        "ve eğitim bilimleri alanında hakemli dergilerde yayımlanmış makale, kitap bölümü ve bildiri gibi çok çeşitli akademik ürünler üretmektedir. "
        "Akademik projeler, bilimsel topluluklarda yürüttüğü görevler ve hakemlik çalışmalarıyla bilimsel topluluğa katkılarını sürdürmektedir."
    )
    st.write(ozgecmis)

# 4. YAYINLAR (EN GÜVENLİ OKUMA SİSTEMİ)
st.divider()
st.subheader("📚 Tüm Akademik Yayınlar")

file_path = "citations.csv"

if os.path.exists(file_path):
    try:
        # CSV dosyasını oku
        df = pd.read_csv(file_
