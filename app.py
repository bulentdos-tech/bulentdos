import streamlit as st

# 1. AYARLAR
st.set_page_config(page_title="Prof. Dr. Bülent DÖŞ", layout="centered")

# 2. TASARIM DOKUNUŞLARI
st.markdown("""
    <style>
    .pub-card { 
        background-color: #f9f9f9; padding: 15px; border-radius: 10px; 
        border-left: 6px solid #D32F2F; margin-bottom: 10px; border: 1px solid #eee;
    }
    .pub-link { color: #D32F2F !important; text-decoration: none; font-weight: bold; }
    .main-title { color: #D32F2F; font-weight: bold; margin-bottom: 0; }
    </style>
    """, unsafe_allow_html=True)

# 3. ÜST GAÜN RESMİ
st.image("https://www.gantep.edu.tr/manset/manset_resim/47941_GAUN_3.jpg")

# 4. PROFİL BÖLÜMÜ
c1, c2 = st.columns([1, 2])
with c1:
    # Profil Fotoğrafı
    try:
        st.image("profil.jpg", width=200)
    except:
        st.image("https://via.placeholder.com/200x250.png?text=Bulent+Dos", width=200)
    
    st.write("### 📱 Sosyal Medya")
    st.markdown("[🔵 LinkedIn](https://www.linkedin.com/in/b%C3%BClent-d%C3%B6%C5%9F-2018a017/)")
    st.markdown("[🔴 Google Scholar](https://scholar.google.com/citations?user=xpLZ0O8AAAAJ)")
    
    # INSTAGRAM KAREKOD (Yüklediğiniz isme göre güncellendi)
    st.write("📸 **Instagram QR**")
    try:
        st.image("instagram karekod.jpeg", width=180)
    except:
        st.caption("QR dosyası bulunamadı. Lütfen GitHub'daki ismin 'instagram karekod.jpeg' olduğundan emin olun.")

with c2:
    st.markdown("<h1 class='main-title'>Prof. Dr. Bülent DÖŞ</h1>", unsafe_allow_html=True)
    st.subheader("Gaziantep Üniversitesi")
    st.write("Eğitim Bilimleri Fakültesi Öğretim Üyesi. Uzmanlık: Üstbiliş, Harmanlanmış Öğrenme, Eğitim Teknolojileri.")
    st.info("✉️ bulentdos@yahoo.com")

# 5. MAKALELER
st.markdown("---")
st.header("📚 Seçilmiş Yayınlar")

titles = [
    "İlköğretim Öğrencilerinin Üstbilişsel Farkındalık Düzeyleri",
    "An Analysis of Teachers' Questioning Strategies",
    "The Analysis of Blogs in Blended Courses"
]
links = [
    "https://dergipark.org.tr/tr/pub/mkusbe/issue/15396/161835",
    "https://academicjournals.org/journal/ERR/article-full-text-pdf/5F8B84161601",
    "https://pau.edu.tr/egetimdergi/tr/makale/the-analysis-of-the-blogs-created-in-a-blended-course-through-the-reflective-thinking-perspective-6"
]

for t, l in zip(titles, links):
    st.markdown(f"""
    <div class='pub-card'>
        <a href='{l}' target='_blank' class='pub-link'>📄 {t}</a>
    </div>
    """, unsafe_allow_html=True)

# 6. ALT BİLGİ
st.markdown("<br><p style='text-align:center; color:gray;'>© 2025 | Prof. Dr. Bülent DÖŞ</p>", unsafe_allow_html=True)
