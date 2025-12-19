import streamlit as st
import pandas as pd
import os

# 1. AYARLAR
st.set_page_config(page_title="Prof. Dr. Bülent DÖŞ", layout="wide")

# 2. ÜST GÖRSEL
st.image("https://www.gantep.edu.tr/manset/manset_resim/47941_GAUN_3.jpg")

# 3. PROFİL VE ÖZGEÇMİŞ
c1, c2 = st.columns([1, 2])

with c1:
    st.image("https://via.placeholder.com/250x300.png?text=Prof.+Bulent+Dos")
    st.link_button("🔴 Google Scholar", "https://scholar.google.com/citations?user=xpLZ0O8AAAAJ")
    st.link_button("🔵 LinkedIn", "https://www.linkedin.com/in/b%C3%BClent-d%C3%B6%C5%9F-2018a017/")
    st.link_button("📸 Instagram", "https://www.instagram.com/bulenttdos/")
    st.info("✉️ bulentdos@yahoo.com")

with c2:
    st.title("Prof. Dr. Bülent DÖŞ")
    bio = "Prof. Dr. Bülent Döş, Gaziantep Üniversitesi Eğitim Fakültesi’nde görev yapan deneyimli bir akademisyendir. "
    bio += "Öğretim programı geliştirme ve eğitim teknolojileri alanında uzmandır. "
    bio += "Google Scholar verilerine göre yaklaşık 970 atıf almıştır. "
    bio += "Lisans ve lisansüstü düzeyde dersler vermekte, çok sayıda teze danışmanlık yapmaktadır. "
    st.write(bio)

# 4. YAYINLAR
st.divider()
st.subheader("📚 Akademik Yayınlar")

path = "citations.csv"

if os.path.exists(path):
    try:
        df = pd.read_csv(path)
        for i in range(len(df)):
            try:
                t = str(df.iloc[i, 0])
                y = str(df.iloc[i, 2])
                st.write(f"**{y}** - {t}")
            except:
                continue
    except:
        st.error("Dosya okunurken hata oluştu.")
else:
    st.warning("citations.csv dosyası bulunamadı.")

st.caption("© 2025 | Prof. Dr. Bülent DÖŞ")
