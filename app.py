import streamlit as st

# 1. SAYFA AYARLARI VE TASARIM
st.set_page_config(page_title="Prof. Dr. Bülent DÖŞ | Resmi Web Sitesi", page_icon="🎓", layout="centered")

st.markdown("""
    <style>
    .main { background-color: #ffffff; }
    .header-text { color: #D32F2F; text-align: center; margin-bottom: 0; }
    .section-title { border-bottom: 2px solid #D32F2F; color: #333; padding-bottom: 8px; margin-top: 35px; font-weight: bold; }
    .pub-card { background-color: #fcfcfc; padding: 15px; border-radius: 12px; border-left: 6px solid #D32F2F; margin-bottom: 15px; border: 1px solid #eee; }
    .contact-badge { background-color: #f1f1f1; padding: 10px; border-radius: 8px; margin-bottom: 10px; border: 1px solid #ddd; }
    </style>
    """, unsafe_allow_html=True)

# --- ÜST KAMPÜS GÖRSELİ ---
st.image("https://www.gantep.edu.tr/manset/manset_resim/47941_GAUN_3.jpg", use_container_width=True)

# --- ANA PROFİL BÖLÜMÜ ---
col1, col2 = st.columns([1, 2])

with col1:
    # LinkedIn veya Yerel Fotoğraf
    try:
        st.image("profil.jpg", width=230)
    except:
        st.image("https://via.placeholder.com/300x350.png?text=Profil+Fotografi", width=230)
    
    st.markdown("### İletişim")
    st.markdown('<div class="contact-badge">📧 bulentdos@yahoo.com</div>', unsafe_allow_html=True)
    st.markdown('<div class="contact-badge">📍 Gaziantep University</div>', unsafe_allow_html=True)
    
    st.markdown("[🔵 LinkedIn](https://www.linkedin.com/in/b%C3%BClent-d%C3%B6%C5%9F-2018a017/)")
    st.markdown("[🔴 Google Scholar](https://scholar.google.com/citations?user=xpLZ0O8AAAAJ)")

with col2:
    st.markdown("<h1 style='color:#D32F2F; margin-top:0;'>Prof. Dr. Bülent DÖŞ</h1>", unsafe_allow_html=True)
    st.markdown("#### Gaziantep Üniversitesi | Eğitim Bilimleri")
    st.write("Eğitim Bilimleri Fakültesi bünyesinde Profesör Doktor olarak görev yapmaktayım. Uzmanlık alanlarım arasında Üstbilişsel Farkındalık, Harmanlanmış Öğrenme, Öğretmen Stratejileri ve Program Geliştirme yer almaktadır.")
    st.info("💡 Temel Yetkinlikler: Eğitim Teknolojileri, Ölçme ve Değerlendirme, Müfredat Geliştirme, Akademik Araştırma Yöntemleri.")

# --- AKADEMİK YAYINLAR ---
st.markdown("<h2 class='section-title'>📚 Seçilmiş Bilimsel Yayınlar</h2>", unsafe_allow_html=True)

publications = [
    {"title": "İlköğretim Öğrencilerinin Üstbilişsel Farkındalık Düzeyleri ve Başarı Analizi", "journal": "Mustafa Kemal Üni. Sosyal
