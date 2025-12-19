import streamlit as st

# 1. SAYFA AYARLARI
st.set_page_config(page_title="Prof. Dr. Bülent DÖŞ", layout="centered")

# 2. ÖZEL STİL (Tasarım ve Link Düzeltmeleri)
st.markdown("""
    <style>
    .pub-card { 
        background-color: #ffffff; padding: 15px; border-radius: 10px; 
        border-left: 6px solid #D32F2F; margin-bottom: 12px; 
        border: 1px solid #eeeeee; box-shadow: 2px 2px 5px rgba(0,0,0,0.05);
    }
    .pub-link { color: #D32F2F !important; text-decoration: none; font-weight: bold; font-size: 1.1rem; }
    .pub-link:hover { text-decoration: underline; color: #b71c1c !important; }
    .social-box { background-color: #f8f9fa; padding: 15px; border-radius: 10px; border: 1px solid #ddd; }
    </style>
    """, unsafe_allow_html=True)

# 3. ÜST GAÜN GÖRSELİ
st.image("https://www.gantep.edu.tr/manset/manset_resim/47941_GAUN_3.jpg", use_container_width=True)

# 4. PROFİL VE SOSYAL MEDYA (YENİ DÜZEN)
col1, col2 = st.columns([1, 1.5])

with col1:
    # Profil Fotoğrafı ve Karekod
    try:
        st.image("profil.jpg", width=200)
    except:
        st.image("https://via.placeholder.com/200x250.png?text=Profil+Foto", width=200)
    
    st.write("📸 **Instagram QR**")
    try:
        st.image("instagram karekod.jpeg", width=180)
    except:
        st.caption("QR: instagram karekod.jpeg")

with col2:
    st.markdown("<h1 style='color:#D32F2F; margin-top:0;'>Prof. Dr. Bülent DÖŞ</h1>", unsafe_allow_html=True)
    st.subheader("Gaziantep Üniversitesi")
    st.write("Eğitim Bilimleri Fakültesi Öğretim Üyesi. Uzmanlık: Üstbiliş, Harmanlanmış Öğrenme, Eğitim Teknolojileri.")
    st.info("✉️ bulentdos@yahoo.com")
    
    # SOSYAL MEDYA LİNKLERİ (SAĞ TARAF)
    st.markdown("### 🔗 Akademik Ağlar")
    st.markdown(f"""
    <div class='social-box'>
        <a href="https://scholar.google.com/citations?user=xpLZ0O8AAAAJ" target="_blank" style="text-decoration:none; font-size:1.1rem;">🔴 <b>Google Scholar Profili</b></a><br><br>
        <a href="https://www.linkedin.com/in/b%C3%BClent-d%C3%B6%C5%9F-2018a017/" target="_blank" style="text-decoration:none; font-size:1.1rem;">🔵 <b>LinkedIn Bağlantısı</b></a>
    </div>
    """, unsafe_allow_html=True)

# 5. SEÇİLMİŞ YAYINLAR (DOĞRUDAN ÇALIŞAN LİNKLER)
st.markdown("---")
st.header("📚 Seçilmiş Yayınlar")

# Yayın Listesi
yayinlar = [
    {"baslik": "İlköğretim Öğrencilerinin Üstbilişsel Farkındalık Düzeyleri", "url": "https://dergipark.org.tr/tr/pub/mkusbe/issue/15396/161835"},
    {"baslik": "An Analysis of Teachers' Questioning Strategies", "url": "https://academicjournals.org/journal/ERR/article-full-text-pdf/5F8B84161601"},
    {"baslik": "The Analysis of Blogs in Blended Courses", "url": "https://pau.edu.tr/egetimdergi/tr/makale/the-analysis-of-the-blogs-created-in-a-blended-course-through-the-reflective-thinking-perspective-6"}
]

for y in yayinlar:
    st.markdown(f"""
    <div class='pub-card'>
        <a href="{y['url']}" target="_blank" class="pub-link">📄 {y['baslik']}</a>
    </div>
    """, unsafe_allow_html=True)

# 6. ALT BİLGİ
st.markdown("<br><p style='text-align:center; color:gray;'>© 2025 | Prof. Dr. Bülent DÖŞ</p>", unsafe_allow_html=True)
