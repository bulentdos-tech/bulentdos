import streamlit as st

# 1. SAYFA YAPILANDIRMASI
st.set_page_config(page_title="Prof. Dr. Bülent DÖŞ | GAÜN", layout="centered")

# 2. ÖZEL TASARIM (GAÜN KIRMIZISI VE MODERN KARTLAR)
st.markdown("""
    <style>
    .main { background-color: #ffffff; }
    .header-style { color: #D32F2F; text-align: center; font-weight: bold; }
    .pub-card { 
        background-color: #f8f9fa; 
        padding: 15px; 
        border-radius: 10px; 
        border-left: 6px solid #D32F2F; 
        margin-bottom: 15px;
        box-shadow: 2px 2px 5px rgba(0,0,0,0.05);
    }
    .pub-link { color: #D32F2F !important; text-decoration: none; font-weight: bold; font-size: 1.1rem; }
    .pub-link:hover { text-decoration: underline; }
    </style>
    """, unsafe_allow_html=True)

# 3. EN ÜST - GAÜN KAMPÜS RESMİ
st.image("https://www.gantep.edu.tr/manset/manset_resim/47941_GAUN_3.jpg", use_container_width=True, caption="Gaziantep Üniversitesi")

# 4. PROFİL BÖLÜMÜ
col1, col2 = st.columns([1, 2])

with col1:
    # Fotoğrafınızı GitHub'a 'profil.jpg' adıyla yüklerseniz burada görünür
    try:
        st.image("profil.jpg", width=220)
    except:
        st.image("https://via.placeholder.com/220x250.png?text=Profil+Foto", width=220)
    
    st.markdown("### 📱 Sosyal Medya")
    st.markdown("[🔵 LinkedIn](https://www.linkedin.com/in/b%C3%BClent-d%C3%B6%C5%9F-2018a017/)")
    st.markdown("[🔴 Google Scholar](https://scholar.google.com/citations?user=xpLZ0O8AAAAJ)")
    
    # INSTAGRAM KAREKOD ALANI
    st.markdown("---")
    st.write("📸 **Instagram QR**")
    try:
        # GitHub'a 'instagram_qr.png' adıyla karekodunuzu yüklerseniz burada görünür
        st.image("instagram_qr.png", width=150)
    except:
        st.info("Karekod için 'instagram_qr.png' dosyasını GitHub'a yükleyin.")

with col2:
    st.markdown("<h1 class='header-style'>Prof. Dr. Bülent DÖŞ</h1>", unsafe_allow_html=True)
    st.subheader("Gaziantep Üniversitesi | Eğitim Fakültesi")
    st.write("""
    Eğitim Bilimleri alanında uzmanlaşmış, harmanlanmış öğrenme, üstbilişsel farkındalık ve 
    eğitim teknolojileri üzerine uluslararası çalışmalar yürüten öğretim üyesiyim.
    """)
    st.info("✉️ İletişim: bulentdos@yahoo.com")
    
    st.markdown("### 🎯 Uzmanlık Alanları")
    st.success("✅ Eğitim Programları ve Öğretim")
    st.success("✅ Dijital Okuryazarlık ve AI")
    st.success("✅ Ölçme ve Değerlendirme")

# 5. MAKALELER (DOĞRUDAN ÇALIŞAN LİNKLER)
st.markdown("---")
st.markdown("<h2 style='color:#333;'>📚 Seçilmiş Yayınlar</h2>", unsafe_allow_html=True)

# Linkleri doğrudan yayıncı sitelerinden (DergiPark vb.) verdim
yayinlar = [
    {
        "ad": "İlköğretim Öğrencilerinin Üstbilişsel Farkındalık Düzeyleri",
        "url": "https://dergipark.
