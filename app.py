import streamlit as st
import pandas as pd
import os

# 1. AYARLAR
st.set_page_config(page_title="Prof. Dr. Bülent DÖŞ", layout="centered")

# 2. ÖZEL STİL
st.markdown("""<style>
.pub-card {background-color: #f9f9f9; padding: 15px; border-radius: 10px; border-left: 5px solid #D32F2F; margin-bottom: 10px; border: 1px solid #eee;}
.pub-title {color: #D32F2F; font-weight: bold; font-size: 1.1rem; margin-bottom: 5px;}
.pub-info {color: #555; font-size: 0.95rem;}
</style>""", unsafe_allow_html=True)

# 3. ÜST GÖRSEL
st.image("https://www.gantep.edu.tr/manset/manset_resim/47941_GAUN_3.jpg")

# 4. PROFİL VE ÖZGEÇMİŞ
col1, col2 = st.columns([1, 2])
with col1:
    st.image("https://via.placeholder.com/200x250.png?text=Bulent+Dos")

with col2:
    st.header("Prof. Dr. Bülent DÖŞ")
    st.write("Gaziantep Üniversitesi Eğitim Fakültesi Öğretim Üyesi.")
    
    # KIRILMAZ ÖZGEÇMİŞ YAPISI
    ozgecmis = (
        "Prof. Dr. Bülent Döş, Gaziantep Üniversitesi Eğitim Fakültesi'nde profesör olarak görev yapan "
        "ve öğretim programları geliştirme, öğretmen eğitimi, yükseköğretimde kalite güvencesi ve "
        "eğitim teknolojileri alanlarında uzmanlaşmış bir akademisyendir. Google Scholar verilerine göre "
        "çalışmaları yaklaşık 970 atıf almış olup, bu durum bilimsel üretimlerinin eğitim bilimleri "
        "literatüründe güçlü bir etki yarattığını göstermektedir. Ulusal ve uluslararası hakemli dergilerde "
        "yayımlanan çok sayıda makalesi, kitap bölümü ve bilimsel bildiri ile alana katkı sunan Döş, "
        "lisans ve lisansüstü düzeyde dersler vermekte; yüksek lisans ve doktora tezlerine danışmanlık "
        "yaparak akademik insan kaynağının yetiştirilmesine katkıda bulunmaktadır."
    )
    st.write(ozgecmis)

# 5. SOSYAL MEDYA
st.markdown("---")
c1, c2, c3 = st.columns(3)
c1.link_button("🔴 Google Scholar", "https://scholar.google.com/citations?user=xpLZ0O8AAAAJ")
c2.link_button("🔵 LinkedIn", "https://www.linkedin.com/in/b%C3%BClent-d%C3%B6%C5%9F-2018a017/")
c3.link_button("📸 Instagram", "https://www.instagram.com/bulenttdos/")

# 6. YAYINLAR
st.markdown("---")
st.subheader("📚 Tüm Akademik Yayınlar")

dosya = "citations.csv"

if os.path.exists(dosya):
    try:
        df = pd.read_csv(dosya)
        df.columns = df.columns.str.strip()
        
        # Sütunları dinamik olarak yakala
        t_col = df.columns[0] # Başlık
        y
