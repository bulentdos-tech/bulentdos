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
    }
    .pub-link { color: #D32F2F; text-decoration: none; font-size: 1.1rem; font-weight: bold; }
    .pub-link:hover { text-decoration: underline; color: #b71c1c; }
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
        st.image("https://via.placeholder.com/210x260.png?text=Profil+Foto", width=210)
    
    st.markdown("### 🔗 Bağlantılar")
    st.markdown("[🔵 LinkedIn Profili](https://www.linkedin.com/in/b%C3%BClent-d%C3%B6%C5%9F-2018a017/)")
    st.markdown("[🔴 Google Scholar](https://scholar.google.com/citations?user=xpLZ0O8AAAAJ)")

with c2:
    st.header("Prof. Dr. Bülent DÖŞ")
    st.subheader("Gaziantep Üniversitesi")
    st.write("Eğitim Bilimleri Fakültesi Öğretim Üyesi. Uzmanlık: Üstbiliş, Harmanlanmış Öğrenme, Eğitim Teknolojileri.")
    st.info("✉️ bulentdos@yahoo.com")

# 5. YAYINLAR (KESİN ÇALIŞAN DOI VE DERGİ LİNKLERİ)
st.markdown("<h2 class='section-title'>📚 Bilimsel Yayınlar</h2>", unsafe_allow_html=True)

# Doğrudan dergi ve makale kaynak linkleri
makaleler = [
    {
        "ad": "İlköğretim Öğrencilerinin Üstbilişsel Farkındalık Düzeyleri", 
        "url": "https://dergipark.org.tr/tr/pub/mkusbe/issue/15396/161835",
        "detay": "Mustafa Kemal Üniversitesi Sosyal Bilimler Dergisi, 2011"
    },
    {
        "ad": "An Analysis of Teachers' Questioning Strategies", 
        "url": "https://academicjournals.org/journal/ERR/article-abstract/5F8B84161601",
        "detay": "Educational Research and Reviews, 2016"
    },
    {
        "ad": "The Analysis of the Blogs Created in a Blended Course", 
        "url": "https://pau.edu.tr/egetimdergi/tr/makale/the-analysis-of-the-blogs-created-in-a-blended-course-through-the-reflective-thinking-perspective-6",
        "detay": "Educational Sciences: Theory and Practice, 2013"
    },
    {
        "ad": "Mobile Phone Use, Metacognitive Awareness and Achievement", 
        "url": "https://www.eurasiajournals.com/index.php/ejer/article/view/114",
        "detay": "European Journal of Educational Research, 2014"
    }
]

for m in makaleler:
    st.markdown(f"""
    <div class='pub-card'>
        <a href='{m['url']}' target='_blank' class='pub-link'>📄 {m['ad']}</a><br>
        <small style='color:#666; display:block; margin-top:5px;'>{m['detay']}</small>
    </div>
    """, unsafe_allow_html=True)

# 6. ALT BİLGİ
st.markdown("<br><hr><p style='text-align:center; color:gray;'>© 2025 | Prof. Dr. Bülent DÖŞ | GAÜN</p>", unsafe_allow_html=True)
