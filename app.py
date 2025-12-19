import streamlit as st
import pandas as pd
import os

# 1. AYARLAR
st.set_page_config(page_title="Prof. Dr. Bülent DÖŞ", layout="centered")

# 2. ÜST GÖRSEL
st.image("https://www.gantep.edu.tr/manset/manset_resim/47941_GAUN_3.jpg")

# 3. PROFİL VE ÖZGEÇMİŞ
col1, col2 = st.columns([1, 2])
with col1:
    st.image("https://via.placeholder.com/200x250.png?text=Bulent+Dos")
    st.link_button("🔴 Google Scholar", "https://scholar.google.com/citations?user=xpLZ0O8AAAAJ")
    st.link_button("🔵 LinkedIn", "https://www.linkedin.com/in/b%C3%BClent-d%C3%B6%C5%9F-2018a017/")
    st.info("bulentdos@yahoo.com")

with col2:
    st.header("Prof. Dr. Bülent DÖŞ")
    # ÖZGEÇMİŞ (GÜVENLİ FORMAT)
    b = "Prof. Dr. Bülent Döş, Gaziantep Üniversitesi Eğitim Fakültesi'nde profesör olarak görev yapan "
    b += "ve öğretim programları geliştirme, öğretmen eğitimi, yükseköğretimde kalite güvencesi ve "
    b += "eğitim teknolojileri alanlarında uzmanlaşmış bir akademisyendir. Google Scholar verilerine göre "
    b += "çalışmaları yaklaşık 970 atıf almış olup, bu durum bilimsel üretimlerinin eğitim bilimleri "
    b += "literatüründe güçlü bir etki yarattığını göstermektedir. Ulusal ve uluslararası hakemli dergilerde "
    b += "yayımlanan çok sayıda makalesi, kitap bölümü ve bilimsel bildiri ile alana katkı sunan Döş, "
    b += "lisans ve lisansüstü düzeyde dersler vermekte; yüksek lisans ve doktora tezlerine danışmanlık "
    b += "yaparak akademik insan kaynağının yetiştirilmesine katkıda bulunmaktadır."
    st.write(b)

# 4. YAYINLAR (EN SADE OKUMA)
st.divider()
st.subheader("📚 Tüm Akademik Yayınlar")

path = "citations.csv"

if os.path.exists(path):
    try:
        df = pd.read_csv(path)
        # Sütunları temizle ve yılları sırala
        df.columns = df.columns.str.strip()
        y_col = df.columns[2]
        df[y_col] = pd.to_numeric(df[y_col], errors='coerce')
        df = df.sort_values(by=y_col, ascending=False)
        
        # Her satırı basitçe yazdır
        for i, row in df.iterrows():
            yil = str(int(row[y_col])) if pd.notna(row[y_col]) else "---"
            st.info(f"📄 {row.iloc[0]} ({yil})")
            
    except Exception as e:
        st.error("Dosya okunurken bir hata oluştu.")
else:
    st.warning("citations.csv dosyası bulunamadı.")

st.caption("© 2025 | Prof. Dr. Bülent DÖŞ")
