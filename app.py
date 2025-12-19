import streamlit as st

# 1. AYARLAR
st.set_page_config(page_title="Prof. Dr. Bülent DÖŞ", layout="centered")

# 2. STİL
st.markdown("""<style>
.stat-card {background-color: #D32F2F; color: white; padding: 15px; border-radius: 10px; text-align: center;}
.pub-card {background-color: #f9f9f9; padding: 10px; border-radius: 8px; border-left: 5px solid #D32F2F; margin-bottom: 10px;}
.pub-link {color: #D32F2F !important; text-decoration: none; font-weight: bold;}
</style>""", unsafe_allow_html=True)

# 3. ÜST GÖRSEL
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
        st.caption("QR dosyası eksik")

with col2:
    st.markdown("<h1 style='color:#D32F2F; margin-top:0;'>Prof. Dr. Bülent DÖŞ</h1>", unsafe_allow_html=True)
    st.write("<b>Gaziantep Üniversitesi Eğitim Bilimleri Fakültesi Öğretim Üyesi.</b>", unsafe_allow_html=True)
    st.write("Eğitim bilimleri alanında uluslararası düzeyde kabul gören çalışmalarıyla tanınan Prof. Dr. Bülent DÖŞ, özellikle Üstbiliş ve Harmanlanmış Öğrenme konularında yaptığı araştırmalarla literatürde 1000'den fazla atıf alarak alanın yönünü tayin etmiştir.")
    
    # SAYILARLA BAŞARI
    ca, cb, cc = st.columns(3)
    ca.markdown("<div class='stat-card'><b>50+</b><br>Yayın</div>", unsafe_allow_html=True)
    cb.markdown("<div class='stat-card'><b>1000+</b><br>Atıf</div>", unsafe_allow_html=True)
    cc.markdown("<div class='stat-card'><b>30+</b><br>Bildiri</div>", unsafe_allow_html=True)

# 5. BAĞLANTILAR
st.markdown("---")
st.markdown("[🔴 Google Scholar](https://scholar.google.com/citations?user=xpLZ0O8AAAAJ) | [🔵 LinkedIn](https://www.linkedin.com/in/b%C3%BClent-d%C3%B6%C5%9F-2018a017/) | 📧 bulentdos@yahoo.com")

# 6. YAYINLAR
st.header("📚 Seçilmiş Yayınlar")
yayin_listesi = [
    ["İlköğretim Öğrencilerinin Üstbilişsel Farkındalık Düzeyleri", "https://dergipark.org.tr/tr/pub/mkusbe/issue/15396/161835"],
    ["An Analysis of Teachers' Questioning Strategies", "https://academicjournals.org/journal/ERR/article-full-text-pdf/5F8B84161601"],
    ["The Analysis of Blogs in Blended Courses", "https://pau.edu.tr/egetimdergi/tr/makale/the-analysis-of-the-blogs-created-in-a-blended-course-through-the-reflective-thinking-perspective-6"]
]

for ad, link in yayin_listesi:
    st.markdown(f"<div class='pub-card'><a href='{link}' target='_blank' class='pub-link'>📄 {ad}</a></div>", unsafe_allow_html=True)

st.markdown("<br><p style='text-align:center; color:gray;'>© 2025 | Prof. Dr. Bülent DÖŞ</p>", unsafe_allow_html=True)
