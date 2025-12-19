import streamlit as st

# 1. AYARLAR
st.set_page_config(page_title="Prof. Dr. Bülent DÖŞ", layout="centered")

# 2. ÜST GÖRSEL
st.image("https://www.gantep.edu.tr/manset/manset_resim/47941_GAUN_3.jpg")

# 3. PROFİL VE ÖZGEÇMİŞ
col1, col2 = st.columns([1, 2])

with col1:
    try:
        st.image("profil.jpg", width=200)
    except:
        st.image("https://via.placeholder.com/200x250.png?text=Bulent+Dos", width=200)

with col2:
    st.header("Prof. Dr. Bülent DÖŞ")
    st.write("Gaziantep Üniversitesi Eğitim Fakültesi’nde görev yapan deneyimli bir akademisyendir; öğretim programı geliştirme, öğretmen eğitimi, yükseköğretim ve eğitim teknolojileri gibi alanlarda odaklanan çalışmalarıyla tanınır.")
    st.write("Google Scholar verilerine göre toplamda yaklaşık 970 atıf almış; bu atıflar onun çalışmalarının eğitim bilimleri literatüründe geniş bir etki yarattığını göstermektedir.")
    st.write("Prof. Dr. Döş, lisans ve lisansüstü düzeyde dersler vermekte, çok sayıda yüksek lisans ve doktora tezine başarıyla danışmanlık yapmaktadır.")

# 4. SOSYAL MEDYA VE İLETİŞİM
st.markdown("---")
c1, c2, c3 = st.columns(3)
c1.link_button("🔴 Google Scholar", "https://scholar.google.com/citations?user=xpLZ0O8AAAAJ")
c2.link_button("🔵 LinkedIn", "https://www.linkedin.com/in/b%C3%BClent-d%C3%B6%C5%9F-2018a017/")
c3.link_button("📸 Instagram", "https://www.instagram.com/bulenttdos/")

st.info("✉️ E-posta: bulentdos@yahoo.com")

# 5. BAŞARI SAYILARI
st.write("### 📊 Akademik Göstergeler")
ca, cb, cc = st.columns(3)
ca.metric("Yayın", "50+")
cb.metric("Atıf", "970+")
cc.metric("Bildiri", "30+")

# 6. YAYINLAR (LİNKLER)
st.markdown("---")
st.subheader("📚 Seçilmiş Yayınlar")

st.link_button("📄 İlköğretim Öğrencilerinin Üstbilişsel Farkındalık Düzeyleri", "https://dergipark.org.tr/tr/pub/mkusbe/issue/15396/161835")
st.write("")
st.link_button("📄 An Analysis of Teachers' Questioning Strategies", "https://academicjournals.org/journal/ERR/article-full-text-pdf/5F8B84161601")
st.write("")
st.link_button("📄 The Analysis of Blogs in Blended Courses", "https://pau.edu.tr/egetimdergi/tr/makale/the-analysis-of-the-blogs-created-in-a-blended-course-through-the-reflective-thinking-perspective-6")

st.markdown("---")
st.caption("© 2025 | Prof. Dr. Bülent DÖŞ | GAÜN")
