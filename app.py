import streamlit as st

# 1. SAYFA AYARLARI
st.set_page_config(page_title="Prof. Dr. Bülent DÖŞ | Resmi Web Sitesi", page_icon="🎓", layout="centered")

# Görsel Stil Düzenlemeleri (GAÜN Kırmızısı ve Modern Fontlar)
st.markdown("""
    <style>
    .main { background-color: #ffffff; }
    .header-text { color: #D32F2F; text-align: center; }
    .section-title { border-bottom: 2px solid #D32F2F; color: #333; padding-bottom: 5px; margin-top: 30px; }
    .social-btn { display: inline-block; padding: 10px 20px; background-color: #f1f1f1; border-radius: 5px; text-decoration: none; color: #333; margin: 5px; }
    .social-btn:hover { background-color: #D32F2F; color: white; }
    </style>
    """, unsafe_allow_html=True)

# --- ÜST BİLGİ / KİMLİK ---
st.markdown("<h1 class='header-text'>Prof. Dr. Bülent DÖŞ</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size: 1.2rem;'>Gaziantep Üniversitesi Eğitim Bilimleri Fakültesi Öğretim Üyesi</p>", unsafe_allow_html=True)

st.image("https://via.placeholder.com/800x300.png?text=Akademik+Calismalar+ve+Vizyon", use_container_width=True) # Buraya bir kampüs veya kütüphane fotoğrafı çok yakışır

# --- HAKKIMDA ---
st.markdown("<h2 class='section-title'>👤 Hakkımda</h2>", unsafe_allow_html=True)
st.write("""
Eğitim bilimleri alanında dijitalleşme, ölçme değerlendirme ve yenilikçi öğrenme yaklaşımları üzerine 
bilimsel araştırmalar yürütmekteyim. Akademik kariyerim boyunca teknoloji entegrasyonu ve 
akran öğrenmesi gibi konularda ulusal ve uluslararası pek çok yayına imza attım.
""")

# --- ÇALIŞMALARIM VE YAYINLARIM ---
col1, col2 = st.columns(2)

with col1:
    st.markdown("<h3 class='section-title'>📚 Makaleler (SSCI/Scopus)</h3>", unsafe_allow_html=True)
    st.markdown("""
    * **Döş, B. (2023).** *Eğitimde Dijital Dönüşüm ve Gelecek.*
    * **Döş, B. & ark. (2022).** *Akran Öğrenmesi Metotları.*
    * **Döş, B. (2021).** *Ölçme ve Değerlendirmede Yeni Yaklaşımlar.*
    """)

with col2:
    st.markdown("<h3 class='section-title'>🎤 Bildiriler & Sunumlar</h3>", unsafe_allow_html=True)
    st.markdown("""
    * **ERPA 2023:** *Eğitimde Yapay Zeka Kullanımı.*
    * **ICOTEL 2022:** *Uzaktan Eğitim Stratejileri.*
    * **Uluslararası Eğitim Kongresi:** *Öğretmen Eğitimi.*
    """)

# --- AKADEMİK PROJELER ---
st.markdown("<h2 class='section-title'>🚀 Yürüttülen Projeler</h2>", unsafe_allow_html=True)
st.info("BAP - Gaziantep Üniversitesi: Eğitimde Dijital Okuryazarlık Seviyelerinin İncelenmesi (Yürütücü)")
st.success("TÜBİTAK 4004: Doğa Eğitimi ve Bilim Okulları Danışmanlığı")

# --- SOSYAL MEDYA VE İLETİŞİM ---
st.markdown("<h2 class='section-title'>📱 Sosyal Medya & Bağlantılar</h2>", unsafe_allow_html=True)

c1, c2, c3, c4 = st.columns(4)
with c1: st.markdown("[🔗 LinkedIn](https://www.linkedin.com/in/bulentdos/)", unsafe_allow_html=True)
with c2: st.markdown("[📊 Google Scholar](https://scholar.google.com/)", unsafe_allow_html=True)
with c3: st.markdown("[🐦 Twitter / X](https://twitter.com/)", unsafe_allow_html=True)
with c4: st.markdown("[📧 E-Posta](mailto:bulentdos@yahoo.com)", unsafe_allow_html=True)

# --- ALT BİLGİ ---
st.markdown("<br><hr><p style='text-align: center; color: gray;'>© 2025 | Prof. Dr. Bülent DÖŞ - Resmi Web Sayfası</p>", unsafe_allow_html=True)
