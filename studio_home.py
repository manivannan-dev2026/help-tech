import streamlit as st
import urllib.parse

st.set_page_config(page_title="Help Tech | Digital Solutions", page_icon="🚀", layout="wide")
st.markdown('<meta name="google-site-verification" content="dDEMtx3tEkGRYrKzCw7UrXi-7MFwOgKNfTtuXFGoEFI" />', unsafe_allow_html=True)

# மேல் மூலையில் தமிழ் / English மொழி மாற்றும் வசதி
lang = st.radio("🌐 மொழி / Language:", ["தமிழ்", "English"], horizontal=True)

txt = {
    "தமிழ்": {
        "brand": "🚀 Help Tech (ஹெல்ப் டெக்)",
        "tagline": "உங்கள் வியாபாரம் மற்றும் அன்றாட வாழ்க்கைக்கு உதவும் நவீன டிஜிட்டல் தீர்வுகள்!",
        "about_h": "💡 எங்களைப் பற்றி (About Help Tech)",
        "about_p": "சென்னையைத் தலைமையிடமாகக் கொண்டு செயல்படும் Help Tech, சிறு வணிகர்கள் மற்றும் பொதுமக்களுக்குப் பயனுள்ள, எளிமையான வெப் ஆப்களை (Web Applications) உருவாக்கித் தரும் ஒரு தொழில்நுட்ப நிறுவனமாகும்.",
        "apps_h": "📱 எங்களின் 3 முக்கியத் தயாரிப்புகள் (Our Products)",
        "bus_desc": "நேரடி GPS இருப்பிடம், பேருந்து கூட்ட நெரிசல் (Crowd Meter) மற்றும் வழித்தட வழிகாட்டி.",
        "bill_desc": "மளிகை, துணிக்கடை, ஹோட்டல் மற்றும் ஒர்க்ஷாப்களுக்கான வாட்ஸ்அப் ஈ-பில் & கணக்கு செயலி.",
        "cal_desc": "தமிழ் & ஆங்கில தேதி, பௌர்ணமி, அமாவாசை, விடுமுறை நாட்கள் மற்றும் அலாரம் ஷெட்யூலர்.",
        "open_btn": "🔗 ஆப்பைத் திறக்க (Open App)",
        "contact_h": "📞 எங்களைத் தொடர்பு கொள்ள (Contact & Demo Request)",
        "name_lbl": "உங்கள் பெயர்:",
        "shop_lbl": "கடை / நிறுவனத்தின் பெயர்:",
        "need_lbl": "எந்த ஆப் தேவை?",
        "wa_btn": "📲 வாட்ஸ்அப் மூலம் தொடர்பு கொள்ள (Chat on WhatsApp)"
    },
    "English": {
        "brand": "🚀 Help Tech",
        "tagline": "Smart, Simple & Affordable Digital Solutions Designed to Help Everyday Life and Businesses!",
        "about_h": "💡 About Help Tech",
        "about_p": "Based in Chennai, Help Tech builds user-friendly, bilingual web applications designed to simplify daily commuting, business billing, and personal productivity.",
        "apps_h": "📱 Our 3 Core Products",
        "bus_desc": "Live crowdsourced GPS location tracking, bus crowd meter, and route finder.",
        "bill_desc": "Paperless WhatsApp E-Bill & permanent sales tracker for Grocery, Textile, Hotel & Workshops.",
        "cal_desc": "Bilingual Tamil & English calendar with Purnima, Amavasya, holidays & activity alarm.",
        "open_btn": "🔗 Launch App",
        "contact_h": "📞 Contact Us / Request a Free Demo",
        "name_lbl": "Your Name:",
        "shop_lbl": "Shop / Business Name:",
        "need_lbl": "Which App are you interested in?",
        "wa_btn": "📲 Connect on WhatsApp"
    }
}[lang]

# முகப்புத் தலைப்பு
st.image("logo.png", width=180)
st.title(txt["brand"])
st.subheader(txt["tagline"])
st.divider()

# எங்களைப் பற்றி
st.markdown(f"### {txt['about_h']}")
st.info(txt["about_p"])

# 3 முக்கிய ஆப்களின் பட்டியல்
st.markdown(f"### {txt['apps_h']}")

col1, col2, col3 = st.columns(3)

with col1:
    with st.container(border=True):
        st.subheader("🚌 Smart Bus Tracker")
        st.write(txt["bus_desc"])
        st.link_button(txt["open_btn"], "https://live-bus-tracker-8fynhysagdjwt8fsedhukg.streamlit.app/", use_container_width=True)

with col2:
    with st.container(border=True):
        st.subheader("🏪 Smart Business Billing")
        st.write(txt["bill_desc"])
        st.link_button(txt["open_btn"], "https://2-shop-billing-stock-app-u4ervgza3mkbmwbvukh3a2.streamlit.app/", use_container_width=True)

with col3:
    with st.container(border=True):
        st.subheader("📅 Smart Tamil Calendar")
        st.write(txt["cal_desc"])
        st.link_button(txt["open_btn"], "https://tamil-smart-calendar-emtfzvksedmjmhrqmxu8cz.streamlit.app/", use_container_width=True)

st.divider()

# வாடிக்கையாளர்கள் தொடர்பு கொள்ளும் பகுதி
st.markdown(f"### {txt['contact_h']}")
with st.form("contact_form"):
    c_name = st.text_input(txt["name_lbl"])
    c_shop = st.text_input(txt["shop_lbl"])
    c_app = st.selectbox(txt["need_lbl"], [
        "🏪 Smart Business Billing App",
        "🚌 Smart Bus Tracker",
        "📅 Smart Tamil Calendar",
        "🛠️ Custom App for My Business"
    ])
    submitted = st.form_submit_button("✅ Prepare WhatsApp Inquiry")
    
    if submitted and c_name:
        msg = urllib.parse.quote(f"வணக்கம் Help Tech! 🙏\nபெயர்: {c_name}\nநிறுவனம்: {c_shop}\nதேவை: {c_app}\nமேலும் விபரங்கள் அறிய விரும்புகிறேன்.")
        st.markdown(f"**[{txt['wa_btn']}](https://wa.me{msg})**")

st.caption("© 2026 Help Tech | Developed by Manivannan K | GitHub: manivannan-dev2026")
