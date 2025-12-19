import streamlit as st
import pandas as pd
import os

# 1. SAYFA AYARLARI
st.set_page_config(page_title="Prof. Dr. Bülent DÖŞ", layout="centered")

# 2. ÖZEL STİL (Yayın kartları için)
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
    try:
        st.image("profil.jpg", width=200)
    except:
        st.image("https://via.placeholder.com/200x250.png?text=Bulent+Dos", width=200)

with col2:
    st.header("Prof. Dr. Bülent DÖŞ")
    st.write("Gaziantep Üniversitesi Eğitim Fakültesi Öğretim Üyesi.")
    st.write("Prof. Dr. Bülent Döş, Gaziantep Üniversitesi Eğitim Fakültesi’nde profesör olarak görev yapan ve
öğretim programları geliştirme, öğretmen eğitimi, yükseköğretimde kalite güvencesi ve eğitim
teknolojileri alanlarında uzmanlaşmış bir akademisyendir. Google Scholar verilerine göre çalışmaları
yaklaşık 970 atıf almış olup, bu durum bilimsel üretimlerinin eğitim bilimleri literatüründe güçlü
bir etki yarattığını göstermektedir. Ulusal ve uluslararası hakemli dergilerde yayımlanan çok sayıda
makalesi, kitap bölümü ve bilimsel bildiri ile alana katkı sunan Döş, lisans ve lisansüstü düzeyde
dersler vermekte; yüksek lisans ve doktora tezlerine danışmanlık yaparak akademik insan kaynağının
yetiştirilmesine katkıda bulunmaktadır. Ayrıca çeşitli bilimsel projelerde yürütücü ve araştırmacı
olarak görev almakta, akademik dergilerde hakemlik ve bilimsel kurul üyelikleri aracılığıyla
akademik topluluğa hizmet etmeyi sürdürmektedir.")

# 5. SOSYAL MEDYA
st.markdown("---")
c1, c2, c3 = st.columns(3)
c1.link_button("🔴 Google Scholar", "https://scholar.google.com/citations?user=xpLZ0O8AAAAJ")
c2.link_button("🔵 LinkedIn", "https://www.linkedin.com/in/b%C3%BClent-d%C3%B6%C5%9F-2018a017/")
c3.link_button("📸 Instagram", "https://www.instagram.com/bulenttdos/")

# 6. TÜM YAYINLAR BÖLÜMÜ
st.markdown("---")
st.subheader("📚 Tüm Akademik Yayınlar")

file_path = "citations.csv"

if os.path.exists(file_path):
    try:
        # CSV dosyasını oku
        df = pd.read_csv(file_path)
        df.columns = df.columns.str.strip() # Sütun isimlerindeki boşlukları temizle
        
        # Dinamik sütun eşleştirme
        title_col = next((c for c in df.columns if 'Title' in c or 'title' in c), df.columns[0])
        author_col = next((c for c in df.columns if 'Author' in c or 'author' in c), df.columns[1])
        year_col = next((c for c in df.columns if 'Year' in c or 'year' in c), df.columns[2])
        journal_col = next((c for c in df.columns if 'Journal' in c or 'Publication' in c or 'Publisher' in c), None)

        # Yılı sayıya çevir ve sırala
        df[year_col] = pd.to_numeric(df[year_col], errors='coerce')
        df = df.sort_values(by=year_col, ascending=False)
        
        # Her yayını kart olarak bas
        for _, row in df.iterrows():
            t = row[title_col]
            a = row[author_col]
            y = int(row[year_col]) if pd.notna(row[year_col]) else "Belirtilmemiş"
            j = row[journal_col] if journal_col and pd.notna(row[journal_col]) else ""
            
            st.markdown(f"""
            <div class="pub-card">
                <div class="pub-title">📄 {t}</div>
                <div class="pub-info"><b>Yazar(lar):</b> {a}</div>
                <div class="pub-info"><b>Yıl:</b> {y} | <b>Yayın:</b> {j}</div>
            </div>
            """, unsafe_allow_html=True)
            
    except Exception as e:
        st.error(f"⚠️ Liste oluşturulurken bir hata oluştu: {e}")
else:
    st.error("❌ 'citations.csv' dosyası bulunamadı.")

st.markdown("---")
st.caption("© 2025 | Prof. Dr. Bülent DÖŞ")
