import streamlit as st
import pandas as pd
import os

# 1. SAYFA AYARLARI
st.set_page_config(page_title="Prof. Dr. Bülent DÖŞ", layout="wide")

# 2. ÖZEL STİL
st.markdown("""<style>
.bio-box { background-color: #fdfdfd; padding: 20px; border-radius: 15px; border: 1px solid #eee; line-height: 1.7; font-size: 1.05rem; color: #333; text-align: justify; }
.pub-card { background-color: #ffffff; padding: 15px; border-radius: 10px; border-left: 5px solid #D32F2F; margin-bottom: 10px; border: 1px solid #eee; box-shadow: 1px 1px 3px rgba(0,0,0,0.05); }
.pub-title { color: #D32F2F; font-weight: bold; font-size: 1.1rem; }
.contact-section { background-color: #f1f1f1; padding: 15px; border-radius: 10px; text-align: center; margin-top: 10px; }
</style>""", unsafe_allow_html=True)

# 3. ÜST GAÜN GÖRSELİ
st.image("https://www.gantep.edu.tr/manset/manset_resim/47941_GAUN_3.jpg", use_container_width=True)

# 4. ÜST PANEL: FOTO VE ÖZGEÇMİŞ
col1, col2 = st.columns([1, 2.5])

with col1:
    try:
        st.image("profil.jpg", width=250)
    except:
        st.image("https://via.placeholder.com/250x300.png?text=Prof.+Dr.+Bulent+Dos", width=250)
    
    st.markdown("<div class='contact-section'>", unsafe_allow_html=True)
    st.link_button("🔴 Google Scholar", "https://scholar.google.com/citations?user=xpLZ0O8AAAAJ", use_container_width=True)
    st.link_button("🔵 LinkedIn", "https://www.linkedin.com/in/b%C3%BClent-d%C3%B6%C5%9F-2018a017/", use_container_width=True)
    st.link_button("📸 Instagram", "https://www.instagram.com/bulenttdos/", use_container_width=True)
    st.write("📧 bulentdos@yahoo.com")
    st.markdown("</div>", unsafe_allow_html=True)

with col2:
    st.markdown("<h1 style='color:#D32F2F;'>Prof. Dr. Bülent DÖŞ</h1>", unsafe_allow_html=True)
    st.markdown("### Gaziantep Üniversitesi | Eğitim Bilimleri Fakültesi")
    
    # TAM ÖZGEÇMİŞ METNİ
    st.markdown(f"""<div class='bio-box'>
    Prof. Dr. Bülent Döş, Gaziantep Üniversitesi Eğitim Fakültesi’nde görev yapan deneyimli bir akademisyendir; 
    öğretim programı geliştirme, öğretmen eğitimi, yükseköğretim ve eğitim teknolojileri gibi alanlarda odaklanan 
    çalışmalarıyla tanınır. Google Scholar verilerine göre toplamda yaklaşık 970 atıf almış; bu atıflar onun 
    çalışmalarının eğitim bilimleri literatüründe geniş bir etki yarattığını göstermektedir. <br><br>
    Ayrıca profilinde yer alan yayınlar arasındaki etki ve üretkenlik ölçütlerine göre bilimsel üretimi düzenli 
    şekilde atıf bulmaktadır; bu göstergeler, akademik çabalarının ulusal ve uluslararası alanda fark edildiğini 
    ortaya koymaktadır. Prof. Dr. Döş, lisans ve lisansüstü düzeyde dersler vermekte, çok sayıda yüksek lisans 
    ve doktora tezine başarıyla danışmanlık yapmakta ve eğitim bilimleri alanında hakemli dergilerde yayımlanmış 
    makale, kitap bölümü ve bildiri gibi çok çeşitli akademik ürünler üretmektedir. Akademik projeler, bilimsel 
    topluluklarda yürüttüğü görevler ve hakemlik çalışmalarıyla bilimsel topluluğa katkılarını sürdürmektedir.
    </div>""", unsafe_allow_html=True)

# 5. AKADEMİK METRİKLER
st.markdown("---")
m1, m2, m3 = st.columns(3)
m1.metric("Toplam Atıf", "970+")
m2.metric("h-endeksi", "16")
m3.metric("i10-endeksi", "23")

# 6. TÜM YAYINLAR (CSV'DEN)
st.markdown("---")
st.subheader("📚 Tüm Akademik Yayınlar")

file_path = "citations.csv"
