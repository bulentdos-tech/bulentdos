import streamlit as st

# 1. AYARLAR
st.set_page_config(page_title="Prof. Dr. Bülent DÖŞ", layout="centered")

# 2. TASARIM AYARLARI
st.markdown("""<style>
.stat-card {background-color: #D32F2F; color: white; padding: 12px; border-radius: 10px; text-align: center; margin-bottom: 10px;}
.pub-card {background-color: #ffffff; padding: 15px; border-radius: 8px; border-left: 5px solid #D32F2F; margin-bottom: 12px; border: 1px solid #eee;}
.direct-link {color: #D32F2F !important; text-decoration: none; font-weight: bold; font-size: 1.1rem;}
.contact-area {background-color: #f8f9fa; padding: 15px; border-radius: 10px; border: 1px solid #e0e0e0; margin: 15px 0;}
.bio-p {font-size: 1.05rem; line-height: 1.6; color: #333; margin-bottom: 10px;}
</style>""", unsafe_allow_html=True)

# 3. ÜST GÖRSEL
st.image("https://www.gantep.edu.tr/manset/manset_resim/47941_GAUN_3.jpg")

# 4. PROFİL VE YENİ ÖZGEÇMİŞ
col1, col2 = st.columns([1, 2.2])

with col1:
    try:
        st.image("profil.jpg", width=200)
    except:
        st.image("https://via.placeholder.com/200x250.png?text=Bulent+Dos", width=200)

with col2:
    st.markdown("<h1 style='color:#D32F2F; margin-top:0;'>Prof. Dr. Bülent DÖŞ</h1>", unsafe_allow_html=True)
    
    # YENİ ÖZGEÇMİŞ METNİ (PARÇALI YAPI)
    st.markdown("<div class='bio-p'>", unsafe_allow_html=True)
    st.write("Prof. Dr. Bülent Döş, Gaziantep Üniversitesi Eğitim Fakültesi’nde görev yapan deneyimli bir akademisyendir; öğretim programı geliştirme, öğretmen eğitimi, yükseköğretim ve eğitim teknolojileri gibi alanlarda odaklanan çalışmalarıyla tanınır.")
    st.write("Google Scholar verilerine göre toplamda yaklaşık 970 atıf almış; bu atıflar onun çalışmalarının eğitim bilimleri literatüründe geniş bir etki yarattığını göstermektedir.")
    st.write("Prof. Dr. Döş, lisans ve lisansüstü düzeyde dersler vermekte, çok sayıda yüksek lisans ve doktora tezine başarıyla danışmanlık yapmakta ve eğitim bilimleri alanında hakemli dergilerde yayımlanmış makale, kitap bölümü ve bildiri gibi çok çeşitli akademik ürünler üretmektedir.")
    st.markdown("</div>", unsafe_allow_html=True)
    
    # SOSYAL MEDYA LİNKLERİ (ÖZGEÇMİŞİN ALTI)
    st.markdown("""
    <div class='contact-area'>
        <a href="https://scholar.google.com/citations?user=xpLZ0O8AAAAJ" target="_blank" style="color:#d93025; font-weight:bold; text-decoration:none;">🔴 Scholar</a> &nbsp; | &nbsp;
        <a href="https://www.linkedin.com/in/b%C3%BClent-d%C3%B6%C5%9F-2018a017/" target="_blank" style="color:#0077b5; font-weight:bold; text-decoration:none;">🔵 LinkedIn</a> &nbsp; | &nbsp;
        <a href="https://www.instagram.com/bulenttdos/" target
