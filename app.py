import streamlit as st

# 1. SAYFA AYARLARI
st.set_page_config(page_title="Prof. Dr. Bülent DÖŞ | Resmi Web Sayfası", page_icon="🎓", layout="centered")

# Görsel Stil Ayarları
st.markdown("""
    <style>
    .main { background-color: #ffffff; }
    .header-text { color: #D32F2F; text-align: center; margin-bottom: 0; }
    .section-title { border-bottom: 2px solid #D32F2F; color: #333; padding-bottom: 5px; margin-top: 30px; font-weight: bold; }
    .pub-card { background-color: #f9f9f9; padding: 15px; border-radius: 8px; border-left: 5px solid #D32F2F; margin-bottom: 10px; }
    </style>
    """, unsafe_allow_html=True)

# --- ÜST KISIM (KAMPÜS FOTOĞRAFI) ---
# GitHub'a 'kampus.jpg' yüklerseniz o görünür, yüklemezseniz varsayılan kampüs resmi gelir.
try:
    st.image("kampus.jpg", use_container_width=True)
except:
    st.image("https://www.gantep.edu.tr/manset/manset_resim/47941_GAUN_3.jpg", use_container_width=True)

# --- KİMLİK BİLGİLERİ ---
st.markdown("<h1 class='header-text'>Prof. Dr. Bülent DÖŞ</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size: 1.2rem; color: #555;'>Gaziantep Üniversitesi Eğitim Bilimleri Fakültesi</p>", unsafe_allow_html=True)

col1, col2 = st.columns([1, 2])
with col1:
    # GitHub'a 'profil.jpg' yüklediğinizde burada görünecektir.
    try:
        st.image("profil.jpg", width=220)
    except:
        st.warning("📷 profil.jpg yüklenmedi")
    
    st.markdown("### İletişim")
    st.write("📧 bulentdos@yahoo.com")
    st.write("📍 Gaziantep / Türkiye")

with col2:
    st.markdown("<h2 style='margin-top:0;'>Hakkımda</h2>", unsafe_allow_html=True)
    st.write("""
    Gaziantep Üniversitesi Eğitim Bilimleri Fakültesi'nde Profesör olarak görev yapmaktayım. 
    Eğitimde üstbilişsel farkındalık, harmanlanmış öğrenme, öğretmen stratejileri ve 
    eğitim teknolojileri üzerine yoğunlaşan akademik çalışmalar yürütüyorum.
    """)
    
    st.markdown("### Uzmanlık Alanları")
    st.success("✅ Eğitim Programları ve Öğretim")
    st.success("✅ Üstbilişsel Farkındalık (Metacognition)")
    st.success("✅ Harmanlanmış Öğrenme (Blended Learning)")

# --- YAYINLAR (GOOGLE SCHOLAR'DAN) ---
st.markdown("<h2 class='section-title'>📚 Seçilmiş Akademik Yayınlar</h2>", unsafe_allow_html=True)

yayinlar = [
    {"baslik": "İlköğretim Öğrencilerinin Üstbilişsel Farkındalık Düzeyleri İle Akademik Başarısı Arasındaki İlişkinin İncelenmesi", "detay": "Mustafa Kemal Üniversitesi Sosyal Bilimler Dergisi, 2011", "atif": "239+"},
    {"baslik": "An Analysis of Teachers' Questioning Strategies", "detay": "Educational Research and Reviews, 2016", "atif": "166"},
    {"baslik": "Assessing Metacognitive Awareness and Learning Strategies in Distance Learning", "detay": "Mustafa Kemal Üniversitesi Sosyal Bilimler Dergisi, 2010", "atif": "97"},
    {"baslik": "The analysis of the blogs created in a blended course through the reflective thinking perspective", "detay": "Educational Sciences: Theory and Practice, 2013", "atif": "87"},
    {"baslik": "The relationship between mobile phone use, metacognitive awareness and academic achievement", "detay": "European Journal of Educational Research, 2014", "atif": "64"}
]

for y in yayinlar:
    with st.container():
        st.markdown(f"""
        <div class='pub-card'>
            <strong>{y['baslik']}</strong><br>
            <small>{y['detay']}</small><br>
            <span style='color: #D32F2F;'>⭐ Atıf Sayısı: {y['atif']}</span>
        </div>
        """, unsafe_allow_html=True)

# --- BİLDİRİLER VE DİĞER ÇALIŞMALAR ---
st.markdown("<h2 class='section-title'>🎤 Bildiriler & Konferanslar</h2>", unsafe_allow_html=True)
st.write("""
* **Procedia-Social and Behavioral Sciences (2015):** Creating online storylines for increasing the knowledge retention.
* **Procedia (2014):** Developing and evaluating a blended learning course.
* **ERPA (Uluslararası Eğitim Kongreleri):** Çeşitli yıllarda sunulan bildiriler.
""")

# --- SOSYAL MEDYA VE AKADEMİK AĞLAR ---
st.markdown("<h2 class='section-title'>📱 Akademik Bağlantılar</h2>", unsafe_allow_html=True)
c1, c2, c3, c4 = st.columns(4)
with c1: st.markdown("[📊 Google Scholar](https://scholar.google.com/citations?user=xpLZ0O8AAAAJ)")
with c2: st.markdown("[🔗 LinkedIn](https://www.linkedin.com/in/bulentdos/)")
with c3: st.markdown("[🔬 ResearchGate](https://www.researchgate.net/)")
with c4: st.markdown("[📧 E-Posta](mailto:bulentdos@yahoo.com)")

# --- ALT BİLGİ ---
st.markdown(f"<br><hr><p style='text-align: center; color: gray;'>© 2025 | Prof. Dr. Bülent DÖŞ | {st.image('https://www.gantep.edu.tr/img/logo.png', width=30) if False else 'GAÜN'}</p>", unsafe_allow_html=True)
