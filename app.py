import streamlit as st
import pandas as pd
import os

# 1. SAYFA AYARLARI
st.set_page_config(page_title="Prof. Dr. Bülent DÖŞ", layout="centered")

# 2. ÖZEL STİL
st.markdown("""<style>
.pub-card {background-color: #f9f9f9; padding: 15px; border-radius: 10px; border-left: 5px solid #D32F2F; margin-bottom: 10px; border: 1px solid #eee;}
.pub-title {color: #D32F2F; font-weight: bold; font-size: 1.1rem; margin-bottom: 5px;}
.bio-text {line-height: 1.6; text-align: justify; color: #333;}
</style>""", unsafe_allow_html=True)

# 3. ÜST GÖRSEL
st.image("https://www.gantep.edu.tr/manset/manset_resim/47941_GAUN_3.jpg")

# 4. PROFİL VE ÖZGEÇMİŞ
col1, col2 = st.columns([1, 2])
with col1:
    st.image("https://via.placeholder.com/200x250.png?text=Bulent+Dos")

with col2:
    st.header("Prof. Dr. Bülent DÖŞ")
    # ÖZGEÇMİŞ METNİ
    b = "Prof. Dr. Bülent Döş, Gaziantep Üniversitesi Eğitim Fakültesi’nde görev yapan deneyimli bir akademisyendir; öğretim programı geliştirme, öğretmen eğitimi, yükseköğretim ve eğitim teknolojileri gibi alanlarda odaklanan çalışmalarıyla tanınır. Google Scholar verilerine göre toplamda yaklaşık 970 atıf almış; bu atıflar onun çalışmalarının eğitim bilimleri literatüründe geniş bir etki yarattığını göstermektedir. Ayrıca profilinde yer alan yayınlar arasındaki etki ve üretkenlik ölçütlerine göre bilimsel üretimi düzenli şekilde atıf bulmaktadır; bu göstergeler, akademik çabalarının ulusal ve uluslararası alanda fark edildiğini ortaya koymaktadır. Prof. Dr. Döş, lisans ve lisansüstü düzeyde dersler vermekte, çok sayıda yüksek lisans ve doktora tezine başarıyla danışmanlık yapmakta ve eğitim bilimleri alanında hakemli dergilerde yayımlanmış makale, kitap bölümü ve bildiri gibi çok çeşitli akademik ürünler üretmektedir. Akademik projeler, bilimsel topluluklarda yürüttüğü görevler ve hakemlik çalışmalarıyla bilimsel topluluğa katkılarını sürdürmektedir."
    st.markdown(f'<div class="bio-text">{b}</div>', unsafe_allow_html=True)

# 5. SOSYAL MEDYA
st.markdown("---")
c1, c2, c3 = st.columns(3)
c1.link_button("🔴 Google Scholar", "https://scholar.google.com/citations?user=xpLZ0O8AAAAJ")
c2.link_button("🔵 LinkedIn", "https://www.linkedin.com/in/b%C3%BClent-d%C3%B6%C5%9F-2018a017/")
c3.link_button("📸 Instagram", "https://www.instagram.com/bulenttdos/")

# 6. YAYINLAR
st.markdown("---")
st.subheader("📚 Tüm Akademik Yayınlar")

path = "citations.csv"
if os.path.exists(path):
    try:
        df = pd.read_csv(path)
        df.columns = df.columns.str.strip()
        t_col = df.columns[0]
        y_col = df
