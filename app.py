import streamlit as st

# 1. SAYFA AYARLARI
st.set_page_config(page_title="Prof. Dr. Bülent DÖŞ", layout="centered")

# 2. ÖZEL STİL (Linkler ve Kartlar için)
st.markdown("""
    <style>
    .section-title { border-bottom: 2px solid #D32F2F; color: #333; font-weight: bold; margin-top: 20px; }
    .pub-link { color: #0073b1; text-decoration: none; font-weight: bold; }
    .pub-link:hover { text-decoration: underline; }
    .pub-card { background-color: #f9f9f9; padding: 15px; border-radius: 10px; border-left: 5px solid #D32F2F; margin-bottom: 10px; }
    </style>
    """, unsafe_allow_html=True)

# 3. ÜST GÖRSEL (GAÜN KAMPÜS)
st.image("https://www.gantep.edu.tr/manset/manset_resim/47941_GAUN_3.jpg")

# 4. PROFİL VE FOTOĞRAF
c1, c2 = st.columns([1, 2])
with c1:
    # GitHub'a yüklediğiniz profil.jpg'yi okur, yoksa placeholder gösterir
    try:
        st.image("profil.jpg", width=200)
    except:
        st.warning("Lütfen profil.jpg dosyasını GitHub'a yükleyin.")
        st.image("https://via.placeholder.com/200x250.png?text=Bulent+Dos", width=200)
    
    st.markdown("### 🔗 Bağlantılar")
    st.markdown("[🔵 LinkedIn Profili](https://www.linkedin.com/in/b%C3%BClent-d%C3%B6%C5%9F-2018a017/)")
    st.markdown("[🔴 Google Scholar](https://scholar.google.com/citations?user=xpLZ0O8AAAAJ)")

with c2:
    st.header("Prof. Dr. Bülent DÖŞ")
    st.subheader("Gaziantep Üniversitesi")
    st.write("Eğitim Bilimleri Fakültesi Öğretim Üyesi. Uzmanlık Alanları: Üstbiliş, Harmanlanmış Öğrenme, Eğitim Teknolojileri.")
    st.info("✉️ bulentdos@yahoo.com")

# 5. LİNKİ MAKALELER
st.markdown("<h2 class='section-title'>📚 Bilimsel Yayınlar (Tıklanabilir)</h2>", unsafe_allow_html=True)

# Makaleler ve Linkleri
makaleler = [
    {"ad": "Üstbilişsel Farkındalık ve Akademik Başarı İlişkisi", "url": "https://scholar.google.com/scholar?cluster=13289053427958564243"},
    {"ad": "An Analysis of Teachers' Questioning Strategies", "url": "https://scholar.google.com/scholar?cluster=16726514838637731215"},
    {"ad": "The Analysis of Blogs in a Blended Course", "url": "https://scholar.google.com/scholar?cluster=15764030646141386121"},
    {"ad": "The relationship between mobile phone use and achievement", "url": "https://scholar.google.com/scholar?cluster=5166468763539825595"}
]

for m in makaleler:
    st.markdown(f"""
    <div class='pub-card'>
        <a href='{m['url']}' target='_blank' class='pub-link'>📄 {m['ad']}</a>
    </div>
    """, unsafe_allow_html=True)

# 6. ALT BİLGİ
st.markdown("<br><hr><p style='text-align:center; color:gray;'>© 2025 | Prof. Dr. Bülent DÖŞ | GAÜN</p>", unsafe_allow_html=True)
