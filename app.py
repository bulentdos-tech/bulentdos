import streamlit as st

# 1. SAYFA AYARLARI VE TASARIM
st.set_page_config(page_title="Prof. Dr. Bülent DÖŞ | Kişisel Web Sitesi", page_icon="🎓", layout="centered")

st.markdown("""
    <style>
    .main { background-color: #ffffff; }
    .header-text { color: #D32F2F; text-align: center; margin-bottom: 0; font-family: 'Arial', sans-serif; }
    .section-title { border-bottom: 2px solid #D32F2F; color: #333; padding-bottom: 8px; margin-top: 35px; font-weight: bold; text-transform: uppercase; letter-spacing: 1px; }
    .pub-card { background-color: #fcfcfc; padding: 20px; border-radius: 12px; border-left: 6px solid #D32F2F; margin-bottom: 15px; shadow: 0 4px 6px rgba(0,0,0,0.1); }
    .contact-badge { background-color: #f1f1f1; padding: 10px; border-radius: 8px; margin-bottom: 10px; border: 1px solid #ddd; }
    </style>
    """, unsafe_allow_html=True)

# --- ÜST KAMPÜS GÖRSELİ ---
st.image("https://www.gantep.edu.tr/manset/manset_resim/47941_GAUN_3.jpg", use_container_width=True)

# --- ANA PROFİL BÖLÜMÜ ---
col1, col2 = st.columns([1, 2])

with col1:
    # LinkedIn Profil Fotoğrafı Alanı (Eğer profiliniz herkese açıksa doğrudan link de çekilebilir)
    # Şimdilik profesyonel bir placeholder koyuyorum, 'profil.jpg' yüklerseniz o devreye girer.
    try:
        st.image("profil.jpg", width=230)
    except:
        st.image("https://media.licdn.com/dms/image/C4D03AQE1NqD1Y_v-Xw/profile-displayphoto-shrink_800_800/0/1516238383842?e=1715817600&v=beta&t=example", width=230)
    
    st.markdown("### İletişim & Ağlar")
    st.markdown("""
    <div class="contact-badge">📧 bulentdos@yahoo.com</div>
    <div class="contact-badge">📍 Gaziantep University</div>
    """, unsafe_allow_html=True)
    
    st.markdown("[🔵 LinkedIn Profilim](https://www.linkedin.com/in/b%C3%BClent-d%C3%B6%C5%9F-2018a017/)")
    st.markdown("[🔴 Google Scholar](https://scholar.google.com/citations?user=xpLZ0O8AAAAJ)")

with col2:
    st.markdown("<h1 style='color:#D32F2F; margin-top:0;'>Prof. Dr. Bülent DÖŞ</h1>", unsafe_allow_html=True)
    st.markdown("#### Gaziantep Üniversitesi | Eğitim Programları ve Öğretim")
    st.write("""
    Eğitim Bil
