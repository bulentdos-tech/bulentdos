import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="Prof. Dr. Bülent DÖŞ", layout="centered")

st.image("https://www.gantep.edu.tr/manset/manset_resim/47941_GAUN_3.jpg")

col1, col2 = st.columns([1, 2])
with col1:
    st.image("https://via.placeholder.com/200x250.png?text=Bulent+Dos")
    st.link_button("🔴 Google Scholar", "https://scholar.google.com/citations?user=xpLZ0O8AAAAJ")
    st.link_button("🔵 LinkedIn", "https://www.linkedin.com/in/b%C3%BClent-d%C3%B6%C5%9F-2018a017/")
    st.link_button("📸 Instagram", "https://www.instagram.com/bulenttdos/")
    st.info("bulentdos@yahoo.com")

with col2:
    st.header("Prof. Dr. Bülent DÖŞ")
    bio = "Prof. Dr. Bülent Döş, Gaziantep Üniversitesi Eğitim Fakültesi’nde görev yapan deneyimli bir akademisyendir; öğretim programı geliştirme, öğretmen eğitimi, yükseköğretim ve eğitim teknolojileri gibi alanlarda odaklanan çalışmalarıyla tanınır. Google Scholar verilerine göre toplamda yaklaşık 970 atıf almış; bu atıflar onun çalışmalarının eğitim bilimleri literatüründe geniş bir etki yarattığını göstermektedir. Ayrıca profilinde yer alan yayınlar arasındaki etki ve üretkenlik ölçütlerine göre bilimsel üretimi düzenli şekilde atıf bulmaktadır; bu göstergeler, akademik çabalarının ulusal ve uluslararası alanda fark edildiğini ortaya koymaktadır. Prof. Dr. Döş, lisans ve lisansüstü düzeyde dersler vermekte, çok sayıda yüksek lisans ve doktora tezine başarıyla danışmanlık yapmakta ve eğitim bilimleri alanında hakemli dergilerde yayımlanmış makale, kitap bölümü ve bildiri gibi çok çeşitli akademik ürünler üretmektedir. Akademik projeler, bilimsel topluluklarda yürüttüğü görevler ve hakemlik çalışmalarıyla bilimsel topluluğa katkılarını sürdürmektedir."
    st.write(bio)

st.divider()
st.subheader("📚 Tüm Akademik Yayınlar")

path = "citations.csv"
if os.path.exists(path):
    try:
        df = pd.read_csv(path)
        df.columns = df.columns.str.strip()
        t_col = df.columns[0]
        y_col = df.columns[2]
        df[y_col] = pd.to_numeric(df[y_col], errors='coerce')
        df = df.sort_values(by=y_col, ascending=False)
        for i, row in df.iterrows():
            st.info(f"📄 {row[t_col]} ({int(row[y_col]) if pd.notna(row[y_col]) else '---'})")
    except Exception as e:
        st.error("Liste yüklenirken bir sorun oluştu.")
else:
    st.warning("citations.csv dosyası bulunamadı.")

st.caption("© 2025 | Prof. Dr. Bülent DÖŞ")
