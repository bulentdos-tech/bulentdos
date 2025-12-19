import streamlit as st

# 1. SAYFA AYARLARI
st.set_page_config(page_title="Prof. Dr. Bülent DÖŞ | Akademik Portfolyo", layout="centered")

# 2. ÖZEL STİL (Prestijli Görünüm)
st.markdown("""
    <style>
    .bio-text { font-size: 1.1rem; line-height: 1.6; color: #333; }
    .stat-card { 
        background-color: #D32F2F; color: white; padding: 20px; 
        border-radius: 12px; text-align: center; font-weight: bold;
    }
    .stat-number { font-size: 2.2rem; display: block; }
    .pub-card { 
        background-color: #ffffff; padding: 15px; border-radius: 10px; 
        border-left: 6px solid #D32F2F; margin-bottom: 12px; border: 1px solid #eee;
    }
    .pub-link { color: #D32F2F !important; text-decoration: none; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

# 3. ÜST GAÜN GÖRSELİ
st.image("https://www.gantep.edu.tr/manset/manset_resim/47941_GAUN_3.jpg", use_container_width=True)

# 4. ÜST BÖLÜM: FOTOĞRAFLAR VE ÖVGÜ DOLU ÖZGEÇMİŞ
col1, col2 = st.columns([1, 2])

with col1:
    # Profil Fotoğrafı
    try:
        st.image("profil.jpg", width=220)
    except:
        st.image("https://via.placeholder.com/220x250.png?text=Bulent+Dos", width=220)
    
    # Instagram Karekod
    st.write("📸 **Instagram QR**")
    try:
        st.image("instagram karekod.jpeg", width=180)
    except:
        st.caption("QR: instagram karekod.jpeg")

with col2:
    st.markdown("<h1 style='color:#D32F2F; margin-top:0;'>Prof. Dr. Bülent DÖŞ</h1>", unsafe_allow_html=True)
    st.markdown("### Vizyoner Eğitim Bilimci & Araştırmacı")
    
    st.markdown("""
    <div class='bio-text'>
    Gaziantep Üniversitesi'nin yetiştirdiği seçkin akademisyenlerden biri olan <b>Prof. Dr. Bülent DÖŞ</b>, 
    eğitim bilimleri alanında uluslararası düzeyde kabul gören çalışmalarıyla tanınmaktadır. 
    Özellikle <b>Üstbiliş (Metacognition)</b> ve <b>Harmanlanmış Öğrenme</b> konularında yaptığı devrim niteliğindeki 
    araştırmalar, literatürde yüzlerce kez atıf alarak (970+) alanın yönünü tayin etmiştir. 
    Eğitimde dijitalleşme ve öğretmen stratejileri konusundaki vizyonuyla, modern eğitim sistemlerinin 
    inşasına liderlik eden bir isimdir.
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    # Sayılarla Başarı (Stat Kartları)
    c_a, c_b, c_c = st.columns(3)
    with c_a:
        st.markdown("<div class='stat-card'><span class='stat-number'>50+</span>Yayın</div>", unsafe_allow_html=True)
    with c_b:
        st.markdown("<div class='stat-card'><span class='stat-number'>1000+</span>
