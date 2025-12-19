import streamlit as st

# 1. AYARLAR
st.set_page_config(page_title="Prof. Dr. Bülent DÖŞ", layout="centered")

# 2. ÖZEL STİL
st.markdown("""
    <style>
    .section-title { border-bottom: 2px solid #D32F2F; color: #333; font-weight: bold; margin-top: 20px; }
    .pub-card { 
        background-color: #ffffff; 
        padding: 15px; 
        border-radius: 10px; 
        border: 1px solid #e0e0e0;
        border-left: 6px solid #D32F2F; 
        margin-bottom: 12px;
        transition: transform 0.2s;
    }
    .pub-card:hover { transform: scale(1.02); background-color: #fff8f8; }
    .pub-link { color: #1a0dab; text-decoration: none; font-size: 1.1rem; font-weight: 500; }
    </style>
    """, unsafe_allow_html=True)

# 3. ÜST GÖRSEL
st.image("https://www.gantep.edu.tr/manset/manset_resim/47941_GAUN_3.jpg")

# 4. PROFİL
c1, c2 = st.columns([1, 2])
with c1:
    try:
        st.image("profil.jpg", width=210)
    except:
        st.image("https://via.placeholder.com/210x260.png?text=Bulent+Dos", width=210)
    
    st.markdown("### 🔗 Bağlantılar")
    st.markdown("[🔵 LinkedIn Profili](https://www.linkedin.com/in/b%C3%BClent-d%C3%B6%C5%9F-2018a017/)")
    st.markdown("[🔴 Google Scholar](https://scholar.google.com/citations?user=xpLZ0O8AAAAJ)")

with c2:
    st.header("Prof. Dr. Bülent DÖŞ")
    st.subheader("Gaziantep Üniversitesi")
    st.write("Eğitim Bilimleri Fakültesi Öğretim Üyesi. Uzmanlık: Üstbiliş, Harmanlanmış Öğrenme, Eğitim Teknolojileri.")
    st.info("✉️ bulentdos@yahoo.com")

# 5. YAYINLAR (DOĞRUDAN GOOGLE SCHOLAR PROFİLİNDEKİ MAKALELER)
st.markdown("<h2 class='section-title'>📚 Bilimsel Yayınlar</h2>", unsafe_allow_html=True)

# Scholar üzerindeki doğrudan yayın linkleri (Daha güvenli linkleme)
makaleler = [
    {
        "ad": "İlköğretim Öğrencilerinin Üstbilişsel Farkındalık Düzeyleri ve Başarı İlişkisi", 
        "url": "https://scholar.google.com/scholar?oi=bibs&cluster=13289053427958564243&btnI=1&hl=tr",
        "detay": "Mustafa Kemal Üniversitesi Sosyal Bilimler Dergisi, 2011"
    },
    {
        "ad": "An Analysis of Teachers' Questioning Strategies", 
        "url": "https://scholar.google.com/scholar?oi=bibs&cluster=16726514838637731215&btnI=1&hl=tr",
        "detay": "Educational Research and Reviews, 2016"
    },
    {
        "ad": "The Analysis of the Blogs Created in a Blended Course", 
        "url": "https://scholar.google.com/scholar?oi=bibs&cluster=15764030646141386121&btnI=1&hl=tr",
        "detay": "Educational Sciences: Theory and Practice, 2013"
    },
    {
        "ad": "The Relationship Between Mobile Phone Use and Academic Achievement", 
        "url": "https://scholar.google.com/scholar?oi=bibs&cluster=5166468763539825595&btnI=1&hl=tr",
        "detay": "European Journal of Educational Research, 2014"
    }
]

for m in makaleler:
    st.markdown(f"""
    <div class='pub-card'>
        <a href='{m['url']}' target='_blank' class='pub-link'>📄 {m['ad']}</a><br>
        <small style='color:#666;'>{m['detay']}</small>
    </div>
    """, unsafe_allow_html=True)

# 6. ALT BİLGİ
st.markdown("<br><hr><p style='text-align:center; color:gray;'>© 2025 | Prof. Dr. Bülent DÖŞ | GAÜN</p>", unsafe_allow_html=True)
