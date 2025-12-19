import streamlit as st

# 1. SAYFA AYARLARI
st.set_page_config(page_title="Prof. Dr. Bülent DÖŞ", layout="centered")

# 2. ÖZEL STİL
st.markdown("""<style>
.stat-card {background-color: #D32F2F; color: white; padding: 12px; border-radius: 10px; text-align: center; margin-bottom: 10px;}
.pub-card {background-color: #ffffff; padding: 15px; border-radius: 8px; border-left: 6px solid #D32F2F; margin-bottom: 12px; border: 1px solid #eee; box-shadow: 2px 2px 5px rgba(0,0,0,0.05);}
.direct-link {color: #D32F2F !important; text-decoration: none; font-weight: bold; font-size: 1.1rem;}
.direct-link:hover {text-decoration: underline;}
.contact-area {background-color: #f8f9fa; padding: 15px; border-radius: 10px; border: 1px solid #e0e0e0; margin: 15px 0;}
.social-link {text-decoration: none; font-weight: bold; font-size: 1rem; margin-right: 15px;}
</style>""", unsafe_allow_html=True)

# 3. ÜST GAÜN RESMİ
st.image("https://www.gantep.edu.tr/manset/manset_resim/47941_GAUN_3.jpg", use_container_width=True)

# 4. PROFİL VE ÖZGEÇMİŞ
col1, col2 = st.columns([1, 2.2])

with col1:
    try:
        st.image("profil.jpg", width=200)
    except:
        st.image("https://via.placeholder.com/200x250.png?text=Bulent+Dos", width=200)

with col2:
    st.markdown("<h1 style='color:#D32F2F; margin-top:0;'>Prof. Dr. Bülent DÖŞ</h1>", unsafe_allow_html=True)
    st.write("<b>Gaziantep Üniversitesi Eğitim Bilimleri Fakültesi Öğretim Üyesi.</b>", unsafe_allow_html=True)
    st.write("Eğitim bilimleri alanında uluslararası çalışmalarıyla tanınan Prof. Dr. Bülent DÖŞ, özellikle Üstbiliş ve Harmanlanmış Öğrenme konularındaki araştırmalarıyla literatürde 10
