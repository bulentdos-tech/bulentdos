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
    try:
        st.image("profil.jpg", width=200)
    except:
        st.image("https://via.placeholder.com/200x250.png?text=Bulent+Dos", width=200)

with col2:
    st.header("Prof. Dr. Bülent DÖŞ")
    st.write("Gaziantep Üniversitesi Eğitim Fakültesi Öğretim Üyesi.")
    st.write("Google Scholar verilerine göre toplamda yaklaşık 970 atıf almış; bu atıflar çalışmalarının literatürde geniş bir etki yarattığını göstermektedir.")

# 4. SOSYAL MEDYA
st.markdown("---")
c1, c2, c3 = st.columns(3)
c1.link_button("🔴 Google Scholar", "https://scholar.google.com/citations?user=xpLZ0O8AAAAJ")
c2.link_button("🔵 LinkedIn", "https://www.linkedin.com/in/b%C3%BClent-d%C3%B6%C5%9F-2018a017/")
c3.link_button("📸 Instagram", "https://www.instagram.com/bulenttdos/")

# 5. YAYINLAR BÖLÜMÜ
st.markdown("---")
st.subheader("📚 Akademik Yayınlar (2024-2025)")

# DOSYA KONTROLÜ VE OKUMA
file_path = "citations.csv"

if not os.path.exists(file_path):
    st.error(f"❌ '{file_path}' dosyası bulunamadı. Lütfen GitHub'a bu isimle yüklediğinizden emin olun.")
    st.info("İpucu: Dosya adının tamamen küçük harf olduğundan ve sonunda .csv uzantısı olduğundan emin olun.")
else:
    try:
        # CSV'yi oku (Ayraç virgül değilse sep=';' eklemek gerekebilir)
        df = pd.read_csv(file_path)
        
        # Yıl sütununu sayıya çevir (hata vermemesi için)
        df['Year'] = pd.to_numeric(df['Year'], errors='coerce')
        
        # Sadece 2024 ve 2025 yıllarını filtrele
        df_filtered = df[df['Year'].isin([2024, 2025])].sort_values(by='Year', ascending=False)
        
        if not df_filtered.empty:
            for index, row in df_filtered.iterrows():
                title = row['Title'] if pd.notna(row['Title']) else "Başlıksız Yayın"
                author = row['Author'] if pd.notna(row['Author']) else "Yazar Belirtilmemiş"
                year = int(row['Year'])
                journal = row['Journal'] if pd.notna(row['Journal']) else ""
                
                st.success(f"**{title}** \n*{author}* ({year}). {journal}")
        else:
            st.warning("Dosyada 2024 veya 2025 yılına ait yayın bulunamadı.")
            
    except Exception as e:
        st.error(f"⚠️ Dosya okuma hatası: {e}")

st.markdown("---")
st.caption("© 2025 | Prof. Dr. Bülent DÖŞ")
