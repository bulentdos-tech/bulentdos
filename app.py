import streamlit as st

# 1. AYARLAR
st.set_page_config(page_title="Prof. Dr. Bülent DÖŞ", layout="centered")

# 2. TASARIM
st.markdown("""<style>
.stat-card {background-color: #D32F2F; color: white; padding: 12px; border-radius: 10px; text-align: center; margin-bottom: 10px;}
.pub-card {background-color: #ffffff; padding: 15px; border-radius: 8px; border-left: 6px solid #D32F2F; margin-bottom: 12px; border: 1px solid #eee;}
.direct-link {color: #D32F2F !important; text-decoration: none; font-weight: bold; font-size: 1.1rem;}
.contact-area {background-color: #f8f9fa; padding: 15px; border-radius: 10px; border: 1px solid #e0e0e0; margin: 15px 0;}
</style>""", unsafe_allow_html=True)

# 3. ÜST GÖRSEL
st.image("https://www.gantep.edu.tr/manset/manset_resim/47941_GAUN_3.jpg")

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
    
    # HATA ALMAMAK İÇİN METNİ PARÇALADIK
    bio = "Eğitim bilimleri alanında uluslararası çalışmalarıyla tanınan Prof. Dr. Bülent DÖŞ, "
    bio += "özellikle Üstbiliş ve Harmanlanmış Öğrenme konularındaki araştırmalarıyla "
    bio += "literatürde 1000'den fazla atıf alarak alanın yönünü tayin etmiştir."
    st.write(bio)
    
    # SOSYAL MEDYA
    st.markdown("""
    <div class='contact-area'>
        <a href="https://scholar.google.com/citations?user=xpLZ0O8AAAAJ" target="_blank" style="color:#d93025; font-weight:bold; text-decoration:none;">🔴 Google Scholar</a> &nbsp; | &nbsp;
        <a href="https://www.linkedin.com/in/b%C3%BClent-d%C3%B6%C5%9F-2018a017/" target="_blank" style="color:#0077b5; font-weight:bold; text-decoration:none;">🔵 LinkedIn</a> &nbsp; | &nbsp;
        <a href="https://www.instagram.com/bulenttdos/" target="_blank" style="color:#e1306c; font-weight:bold; text-decoration:none;">📸 Instagram</a>
        <br><br>📧 <b>E-posta:</b> bulentdos@yahoo.com
    </div>
    """, unsafe_allow_html=True)
    
    # SAYILAR
    ca, cb, cc = st.columns(3)
    ca.markdown("<div class='stat-card'><b>50+</b><br>Yayın</div>", unsafe_allow_html=True)
    cb.markdown("<div class='stat-card'><b>1000+</b><br>Atıf</div>", unsafe_allow_html=True)
    cc.markdown("<div class='stat-card'><b>30+</b><br>Bildiri</div>", unsafe_allow_html=True)

# 5. YAYINLAR
st.markdown("---")
st.header("📚 Seçilmiş Yayınlar")

st.markdown("""
<div class='pub-card'><a href="https://dergipark.org.tr/tr/pub/mkusbe/issue/15396/161835" target="_blank" class="direct-link">📄 Üstbilişsel Farkındalık ve Başarı Analizi</a></div>
<div class='pub-card'><a href="https://academicjournals.org/journal/ERR/article-full-text-pdf/5F8B84161601" target="_blank" class="direct-link">📄 Analysis of Teachers' Questioning Strategies</a></div>
<div class='pub-card'><a href="https://pau.edu.tr/egetimdergi/tr/makale/the-analysis-of-the-blogs-created-in-a-blended-course-through-the-reflective-thinking-perspective-6" target="_blank" class="direct-link">📄 Analysis of Blogs in Blended Courses</a></div>
""", unsafe_allow_html=True)

st.markdown("<br><p style='text-align:center; color:gray;'>© 2025 | Prof. Dr. Bülent DÖŞ</p>", unsafe_allow_html=True)
