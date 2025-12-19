import streamlit as st

# 1. AYARLAR
st.set_page_config(page_title="Prof. Dr. Bülent DÖŞ", layout="centered")

# 2. STİL
st.markdown("""
    <style>
    .section-title { border-bottom: 2px solid #D32F2F; color: #333; font-weight: bold; margin-top: 20px; }
    .pub-card { background-color: #f9f9f9; padding: 10px; border-radius: 10px; border-left: 5px solid #D32F2F; margin-bottom: 10px; }
    </style>
    """, unsafe_allow_html=True)

# 3. ÜST GÖRSEL
st.image("https://www.gantep.edu.tr/manset/manset_resim/47941_GAUN_3.jpg")

# 4. PROFİL
c1, c2 = st.columns([1, 2])
with c1:
    st.image("https://via.placeholder.com/200x250.png?text=Profil", width=200)
    st.markdown("[🔵 LinkedIn](https://www.linkedin.com/in/b%C3%BClent-d%C3%B6%C5%9F-2018a017/)")
    st.markdown("[🔴 Scholar](https://scholar.google.com/citations?user=xpLZ0O8AAAAJ)")

with c2:
    st.header("Prof. Dr. Bülent DÖŞ")
    st.subheader("Gaziantep Üniversitesi")
    st.write("Eğitim Bilimleri Fakültesi Öğretim Üyesi. Uzmanlık: Üstbiliş, Harmanlanmış Öğrenme ve Eğitim Teknolojileri.")
    st.info("✉️ bulentdos@yahoo.com")

# 5. YAYINLAR (HATA ALMAMAK İÇİN KISA TUTULDU)
st.markdown("<h2 class='section-title'>📚 Öne Çıkan Yayınlar</h2>", unsafe_allow_html=True)

m1 = "Üstbilişsel Farkındalık ve Başarı Analizi (2011) - Atıf: 239"
m2 = "Analysis of Teachers' Questioning Strategies (2016) - Atıf: 166"
m3 = "Analysis of Blogs in Blended Courses (2013) - Atıf: 87"

for m in [m1, m2, m3]:
    st.markdown(f"<div class='pub-card'>{m}</div>", unsafe_allow_html=True)

# 6. PROJELER VE BİLDİRİLER
col_a, col_b = st.columns(2)
with col_a:
    st.markdown("<h3 class='section-title'>🎤 Bildiriler</h3>", unsafe_allow_html=True)
    st.write("- Creating online storylines (2015)")
    st.write("- Blended learning evaluation (2014)")

with col_b:
    st.markdown("<h3 class='section-title'>🚀 Projeler</h3>", unsafe_allow_html=True)
    st.write("- Eğitimde Dijital Okuryazarlık")
    st.write("- Öğretmen Öz-Yeterlilik Analizi")

st.markdown("<br><hr><p style='text-align:center;'>© 2025 | GAÜN</p>", unsafe_allow_html=True)
