import streamlit as st
from streamlit_lottie import st_lottie
import requests
from PIL import Image
from io import BytesIO
import base64

st.set_page_config(page_title="Shiva ⸱Machinhe Learning & Rust & Systems Dev", page_icon="⚙️", layout="wide")

@st.cache_data(show_spinner=False)
def fetch_json(url: str, timeout=8):
    r = requests.get(url, timeout=timeout)
    r.raise_for_status()
    return r.json()

@st.cache_data(show_spinner=False)
def fetch_image_bytes(url: str, timeout=8):
    r = requests.get(url, timeout=timeout)
    r.raise_for_status()
    return r.content

def image_from_bytes(b: bytes):
    return Image.open(BytesIO(b))

CSS = """
:root{
  --accent: #FF6B6B;
  --bg: #f6f8fb;
  --card: #ffffff;
  --muted: #546e7a;
  --text: #0b1220;
}
@media (prefers-color-scheme: dark) {
  :root{
    --bg: #0f1724;
    --card: #0b1220;
    --muted: #9aa4b2;
    --text: #e6eef8;
  }
}
body {
  background: radial-gradient(1200px 600px at 10% 10%, rgba(255,107,107,0.03), transparent),
              radial-gradient(900px 400px at 90% 90%, rgba(0,150,255,0.02), transparent);
  color: var(--text);
}
.card{
  background:var(--card);
  padding:14px;
  border-radius:10px;
  box-shadow:0 6px 18px rgba(2,6,23,0.08);
  transition: transform .18s ease, box-shadow .18s ease;
}
.card:hover{ transform:translateY(-4px); box-shadow:0 10px 30px rgba(2,6,23,0.12); }
.project-title{ font-size:16px; font-weight:700; }
.tag{ display:inline-block; padding:5px 8px; margin-right:6px; margin-top:8px; border-radius:999px; background:rgba(255,255,255,0.03); font-size:12px; }
.download-btn{ padding:8px 14px; background:linear-gradient(90deg,#ff6b6b,#ff9a6b); color:white; border-radius:10px; text-decoration:none; }
footer { visibility: hidden; }
"""
st.markdown(f"<style>{CSS}</style>", unsafe_allow_html=True)

col1, col2 = st.columns([2,3])
with col1:
    st.markdown("Machine Learning & Rust")
    st.markdown("**Building fast, reliable Machine Leaning Algorithms using Rust.**")
    st.markdown("[Resume](#replace-with-your-resume-link) · [✉️ Email](mailto:shivamanoharareddy05@gmail.com)")

with col2:
    st.image("https://via.placeholder.com/640x300.png?text=Shiva+Hero", use_container_width=True)
    try:
        lottie = fetch_json("https://assets9.lottiefiles.com/packages/lf20_jcikwtux.json")
        st_lottie(lottie, height=260, key="hero_lottie")
    except Exception:
        pass

st.markdown("---")

st.markdown("## Selected Projects")
projects = [
    {"title": "rust-wasm-game-engine", "desc": "Tiny fast 2D engine (WASM).", "tags": ["Rust","WASM","Graphics"], "image": "https://via.placeholder.com/400x240.png?text=Project+1", "link": "https://github.com/yourusername/rust-wasm-game-engine"},
    {"title": "fast-logger", "desc": "Zero-alloc logger for telemetry.", "tags": ["Rust","Logging","Perf"], "image": "https://via.placeholder.com/400x240.png?text=Project+2", "link": "https://github.com/yourusername/fast-logger"},
    {"title": "embedded-sensor-node", "desc": "Low-power sensor node with OTA.", "tags": ["Embedded","Rust","Low-Power"], "image": "https://via.placeholder.com/400x240.png?text=Project+3", "link": "https://github.com/yourusername/embedded-sensor-node"}
]

cols = st.columns(3)
for i, p in enumerate(projects):
    with cols[i % 3]:
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        try:
            img_bytes = fetch_image_bytes(p["image"])
            img = image_from_bytes(img_bytes)
            st.image(img, use_container_width=True, clamp=True)
        except Exception:
            pass
        tags_html = "".join([f"<span class='tag'>{t}</span>" for t in p['tags']])
        inner = f"""
        <div style='padding:10px'>
          <div class='project-title'>⚙️ {p['title']}</div>
          <div style='margin-top:6px'>{p['desc']}</div>
          <div style='margin-top:8px'>{tags_html}</div>
          <div style='margin-top:10px'><a href='{p['link']}' target='_blank'>🔗 View on GitHub</a></div>
        </div>
        """
        st.markdown(inner, unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

st.markdown("---")
st.markdown("## About Me")
st.write("I build machine algorithms in rust and julia, hobby OS experiments, and Rust libraries. I focus on performance, correctness, and clean APIs.")

st.markdown("### 🕒 Timeline")
st.markdown("- 2024 ⸱ Started serious Rust projects \n- 2025 ⸱ Built a auto data cleaning python module")

st.markdown("---")
st.markdown("## 📬 Get in touch")
c1, c2 = st.columns([2,1])
with c1:
    _ = st.text_input("Name")
    _ = st.text_input("Email")
    _ = st.text_area("Message")
    if st.button("Send message"):
        st.success("Thanks — I'll get back to you soon.")
with c2:
    st.markdown("**Quick links**")
    st.markdown("- 🐙 [GitHub](https://github.com/yourusername)")
    st.markdown("- 🐦 [Twitter](https://twitter.com/yourhandle)")
    st.markdown("- 💼 [LinkedIn](https://linkedin.com/in/yourprofile)")
