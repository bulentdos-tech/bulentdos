import streamlit as st

# 1. SAYFA AYARLARI
st.set_page_config(page_title="Prof. Dr. Bülent DÖŞ", layout="centered")

# 2. ÖZEL STİL
st.markdown("""<style>
.stat-card {background-color: #D32F2F; color: white; padding: 10px; border-radius: 10px; text-align: center; margin-bottom: 10px;}
.pub-card {background-color: #f9f9f9; padding: 12px; border-radius: 8px; border-left: 5px solid #D32F2F; margin-bottom: 10px;}
.direct-link {color: #D32F2F !important; text-decoration: none; font-weight: bold; font-size: 1.1rem;}
.contact-links {background-color: #f1f1f1; padding: 10px; border-radius: 5px; margin-top: 10px; display: inline-block;}
</style>""", unsafe_allow_html=True)

# 3. ÜST GAÜN RESMİ
st.image("https://www.gantep.edu.tr/manset/manset_resim/47941_GAUN_3.jpg")

# 4. PROFİL VE ÖZGEÇMİŞ
col1, col2 = st.columns([1, 2])

with col1:
    try:
        st.image("profil.jpg", width=200)
    except:
        st.image("https://via.placeholder.com/200x250.png?text=Profil", width=200)
    
    st.write("📸 **Instagram QR**")
    try:
        st.image("instagram karekod.jpeg", width=180)
    except:
        st.caption("instagram karekod.jpeg bulunamadı")

with col2:
    st.markdown("<h1 style='color:#D32F2F; margin-top:0;'>Prof. Dr. Bülent DÖŞ</h1>", unsafe_allow_html=True)
    st.write("<b>Gaziantep Üniversitesi Eğitim Bilimleri Fakültesi Öğretim Üyesi.</b>", unsafe_allow_html=True)
    st.write("Eğitim bilimleri alanında uluslararası çalışmalarıyla tanınan Prof. Dr. Bülent DÖŞ, özellikle Üstbiliş ve Harmanlanmış Öğrenme konularındaki araştırmalarıyla literatürde 1000'den fazla atıf alarak alanın önünü tayin etmiştir.")
    
    # İLETİŞİM LİNKLERİ (ÖZGEÇMİŞİN HEMEN ALTI)
    st.markdown("""
    <div class='contact-links'>
        <a href="https://scholar.google.com/citations?user=xpLZ0O8AAAAJ" target="_blank">🔴 Google Scholar</a> | 
        <a href="https://www.linkedin.com/in/b%C3%BClent-d%C3%B6%C5%9F-2018a017/" target="_blank">🔵 LinkedIn</a> | 
        📧 bulentdos@yahoo.com
    </div>
    """, unsafe_allow_html=True)
    
    st.write("---")
    # BAŞARI SAYILARI
    ca, cb, cc = st.columns(3)
    ca.markdown("<div class='stat-card'><b>50+</b><br>Yayın</div>", unsafe_allow_html=True)
    cb.markdown("<div class='stat-card'><b>1000+</b><br>Atıf</div>", unsafe_allow_html=True)
    cc.markdown("<div class='stat-card'><b>30+</b><br>Bildiri</div>", unsafe_allow_html=True)

# 5. YAYINLAR
st.markdown("---")
st.header("📚 Seçilmiş Yayınlar")

# Linkleri doğrudan HTML a tag'i ile veriyoruz (En güvenli yol)
st.markdown("""
<div class='pub-card'><a href="https://dergipark.org.tr/tr/pub/mkusbe/issue/15396/161835" target="_blank" class="direct-link">📄 İlköğretim Öğrencilerinin Üstbilişsel Farkındalık Düzeyleri</a></div>
<div class='pub-card'><a href="https://academicjournals.org/journal/ERR/article-full-text-pdf/5F8B84161601" target="_blank" class="direct-link">📄 An Analysis of Teachers' Questioning Strategies</a></div>
<div class='pub-card'><a href="https://pau.edu.tr/egetimdergi/tr/makale/the-analysis-of-the-blogs-created-in-a-blended-course-through-the-reflective-thinking-perspective-6" target="_blank" class="direct-link">📄 The Analysis of Blogs in Blended Courses</a></div>
""", unsafe_allow_html=True)

st.markdown("<br><p style='text-align:center; color:gray;'>© 2025 | Prof. Dr. Bülent DÖŞ</p>", unsafe_allow_html=True)
