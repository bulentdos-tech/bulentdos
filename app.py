import streamlit as st
import pandas as pd
import os

# 1. SAYFA AYARLARI
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

file_path = "citations.csv"

if os.path.exists(file_path):
    try:
        # CSV dosyasını oku
        df = pd.read_csv(file_path)
        
        # Sütun isimlerindeki boşlukları ve hataları temizle
        df.columns = df.columns.str.strip()
        
        # Sütun isimlerini tahmin etmeye çalış (Title, Author, Year içerenleri bul)
        # Eğer bulamazsa 1., 2. ve 3. sütunları kullan
        title_col = next((c for c in df.columns if 'Title' in c or 'title' in c), df.columns[0])
        author_col = next((c for c in df.columns if 'Author' in c or 'author' in c), df.columns[1])
        year_col = next((c for c in df.columns if 'Year' in c or 'year' in c), df.columns[2])
        journal_col = next((c for c in df.columns if 'Journal' in c or 'Publication' in c), df.columns[3] if len(df.columns)>3 else df.columns[0])

        # Yıl sütununu sayıya çevir
        df[year_col] = pd.to_numeric(df[year_col], errors='coerce')
        
        # 2024 ve 2025 filtrele
        df_filtered = df[df[year_col].isin([2024, 2025])].sort_values(by=year_col, ascending=False)
        
        if not df_filtered.empty:
            for _, row in df_filtered.iterrows():
                t = row[title_col]
                a = row[author_col]
                y = int(row[year_col])
                j = row[journal_col] if journal_col in row else ""
                
                st.success(f"**{t}** \n\n*{a}* ({y}) \n\n{j}")
        else:
            st.warning("Dosyada 2024 veya 2025 yılına ait yayın bulunamadı.")
            
    except Exception as e:
        st.error(f"⚠️ Veri işleme hatası: {e}")
        st.info("Lütfen CSV dosyanızın içeriğini kontrol edin.")
else:
    st.error("Dosya bulunamadı.")

st.markdown("---")
st.caption("© 2025 | Prof. Dr. Bülent DÖŞ")
