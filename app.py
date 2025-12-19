import streamlit as st
import pandas as pd

# 1. AYARLAR
st.set_page_config(page_title="Prof. Dr. Bülent DÖŞ", layout="centered")

# 2. ÜST GÖRSEL
st.image("https://www.gantep.edu.tr/manset/manset_resim/47941_GAUN_3.jpg")

# 3. PROFİL VE ÖZGEÇMİŞ
col1, col2 = st.columns([1, 2])

with col1:
    try:
        st.image("profil.jpg", width=200)
    except:
        st.image("https://via.placeholder.com/200x250.png?text=Bulent+Dos", width=200)

with col2:
    st.header("Prof. Dr. Bülent DÖŞ")
    st.write("Gaziantep Üniversitesi Eğitim Fakültesi’nde görev yapan deneyimli bir akademisyendir; öğretim programı geliştirme, öğretmen eğitimi, yükseköğretim ve eğitim teknolojileri alanlarında uzmandır.")
    st.write("Akademik çalışmaları eğitim bilimleri literatüründe geniş bir etki yaratmış olup, uluslararası alanda saygın yayın evleri ve dergilerde yer almıştır.")

# 4. SOSYAL MEDYA VE İLETİŞİM
st.markdown("---")
c1, c2, c3 = st.columns(3)
c1.link_button("🔴 Google Scholar", "https://scholar.google.com/citations?user=xpLZ0O8AAAAJ")
c2.link_button("🔵 LinkedIn", "https://www.linkedin.com/in/b%C3%BClent-d%C3%B6%C5%9F-2018a017/")
c3.link_button("📸 Instagram", "https://www.instagram.com/bulenttdos/")
st.info("✉️ E-posta: bulentdos@yahoo.com")

# 5. YAYINLAR BÖLÜMÜ (CSV DOSYASINDAN OKUMA)
st.markdown("---")
st.subheader("📚 Akademik Yayınlar")

try:
    # CSV dosyasını oku
    df = pd.read_csv("citations.csv")
    
    # Sadece 2024 ve 2025 yılına ait olanları filtrele
    # (Not: CSV dosyanızdaki yıl sütununa göre ayarlanmıştır)
    df_filtered = df[df['Year'].isin([2024, 2025])].sort_values(by='Year', ascending=False)
    
    if not df_filtered.empty:
        for index, row in df_filtered.iterrows():
            # Makale formatını oluştur
            yayin_metni = f"**{row['Title']}** \n*{row['Author']}* ({row['Year']}). {row['Journal']}"
            
            # Eğer makale ise yeşil kutuda, değilse mavi kutuda göster
            if "Journal Article" in str(row['Article type']):
                st.success(yayin_metni)
            else:
                st.info(yayin_metni)
    else:
        st.warning("2024 veya 2025 yılına ait yayın bulunamadı.")

except Exception as e:
    st.error("Yayınlar listelenirken bir hata oluştu. Lütfen citations.csv dosyasının yüklendiğinden emin olun.")

st.markdown("---")
st.caption("© 2025 | Prof. Dr. Bülent DÖŞ | GAÜN")
