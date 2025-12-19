import streamlit as st
import pandas as pd
import os

# 1. AYARLAR
st.set_page_config(page_title="Prof. Dr. Bülent DÖŞ", layout="wide")

# 2. ÜST GÖRSEL
st.image("https://www.gantep.edu.tr/manset/manset_resim/47941_GAUN_3.jpg")

# 3. PROFİL VE ÖZGEÇMİŞ
c1, c2 = st.columns([1, 2.5])

with c1:
    st.image("https://via.placeholder.com/250x300.png?text=Prof.+Dr.+Bulent+Dos")
    st.link_button("🔴 Google Scholar", "https://scholar.google.com/citations?user=xpLZ0O8AAAAJ")
    st.link_button("🔵 LinkedIn", "https://www.linkedin.com/in/b%C3%BClent-d%C3%B6%C5%9F-2018a017/")
    st.link_button("📸 Instagram", "https://www.instagram.com/bulenttdos/")
    st.info("📧 bulentdos@yahoo.com")

with c2:
    st.title("Prof. Dr. Bülent DÖŞ")
    # Özgeçmiş metni
    txt = "Prof. Dr. Bülent Döş, Gaziantep Üniversitesi Eğitim Fakültesi’nde görev yapan deneyimli bir akademisyendir; öğretim programı geliştirme, öğretmen eğitimi, yükseköğretim ve eğitim teknolojileri gibi alanlarda odaklanan çalışmalarıyla tanınır. Google Scholar verilerine göre toplamda yaklaşık 970 atıf almış; bu atıflar onun çalışmalarının eğitim bilimleri literatüründe geniş bir etki yarattığını göstermektedir. Ayrıca profilinde yer alan yayınlar arasındaki etki ve üretkenlik ölçütlerine göre bilimsel üretimi düzenli şekilde atıf bulmaktadır; bu göstergeler, akademik çabalarının ulusal ve uluslararası alanda fark edildiğini ortaya koymaktadır. Prof. Dr. Döş, lisans ve lisansüstü düzeyde dersler vermekte, çok sayıda yüksek lisans ve doktora tezine başarıyla danışmanlık yapmakta ve eğitim bilimleri alanında hakemli dergilerde yayımlanmış makale, kitap bölümü ve bildiri gibi çok çeşitli akademik ürünler üretmektedir. Akademik projeler, bilimsel topluluklarda yürüttüğü görevler ve hakemlik çalışmalarıyla bilimsel topluluğa katkılarını sürdürmektedir."
    st.write(txt)

# 4. YAYINLAR
st.divider()
st.subheader("📚 Tüm Akademik Yayınlar")

f_path = "citations.csv"

if os.path.exists(f_path):
    try:
        # En basit okuma yöntemi
        data = pd.read_csv(f_path)
        # Sadece başlıkları göster (Hata riskini azaltmak için)
        for i in range(len(data)):
            try:
                row_title = str(data.iloc[i, 0])
                row_year = str(data.iloc[i, 2])
                st.markdown(f"**{row_year}** - {row_title}")
            except:
                continue
    except:
        st.error("Dosya okunurken bir hata oluştu.")
else:
    st.error("citations.csv dosyası bulunamadı.")

st.caption("© 2025 | Prof. Dr. Bülent DÖ
