import streamlit as st
from PIL import Image
from pathlib import Path

# --- UI Cleanup ---
st.markdown(""" 
<style> 
#MainMenu, footer, header {visibility: hidden;} 
[data-testid="stSidebar"] { display: none; }
</style> 
""", unsafe_allow_html=True)

# --- Top Spacer ---
st.markdown("<div style='margin-top: 50px;'></div>", unsafe_allow_html=True)

# --- Top Border Image ---
top_col1, top_col2, top_col3 = st.columns([1, 4, 1])
with top_col2:
    st.image("images/border.png", width=4000)

# --- Layout Tweak ---
st.markdown("""
<style>
.block-container {
    padding-top: 20px;
    margin-top: -60px;
}
</style>
""", unsafe_allow_html=True)

# --- Styling ---
st.markdown("""
<style>
body {
    background-image: url("https://i.imgur.com/tLJUZFt.png");
    background-size: cover;
    background-attachment: fixed;
}

h1, h3 {
    color: #ffffff;
    font-family: Georgia;
}

.sat-btn {
    background-color: #ffffff;
    color: #000000;
    border: 2px solid #000000;
    padding: 12px 20px;
    border-radius: 8px;
    font-weight: bold;
    font-size: 17px;
    width: 100%;
    cursor: pointer;
    box-shadow: 0 2px 6px rgba(0,0,0,0.15);
    font-family: Georgia;
}

.sat-btn:hover {
    background-color: #f0f0f0;
}
</style>
""", unsafe_allow_html=True)

# --- Title Section (shifted upward slightly) ---
st.markdown("""
<div style='text-align:center; padding-top:-30px; margin-top:-20px;'>
    <h1 style='font-size:32px; font-family: Georgia;'>SXM Satellite Directory</h1>
    <h3 style='font-size:18px;font-family: Georgia;'>Choose your satellite below</h3>
</div>
""", unsafe_allow_html=True)

# --- Satellite Data with External URLs ---
satellite_data = [
    {
        "image_path": "images/image.png",
        "button_label": "Go to SXM 7/8",
        "url": "https://sxmdocumentation.streamlit.app/"
    },
    {
        "image_path": "images/satellite1.png",
        "button_label": "Go to SXM 9/10",
        "url": "https://sxmdocumentation.streamlit.app/"
    },
    {
        "image_path": "images/satellite2.png",
        "button_label": "Go to SXM 11/12",
        "url": "https://sxmdocumentation.streamlit.app/"
    }
]

# --- Image Resolution Helper ---
def resolve_image_path(path_str):
    image_path = Path(path_str)
    if image_path.exists():
        return image_path
    fallback_path = Path(__file__).parent / path_str
    if fallback_path.exists():
        return fallback_path
    st.warning(f"⚠️ Could not locate image: {path_str}")
    return None

# --- Image Row ---
image_cols = st.columns([1, 0.05, 1, 0.05, 1])
for i, sat in enumerate(satellite_data):
    with image_cols[i * 2]:
        try:
            img = Image.open(sat["image_path"])
            st.image(img, use_container_width=False, width=360)
        except FileNotFoundError:
            st.error(f"🚫 Image not found: {sat['image_path']}")
            resolve_image_path(sat["image_path"])

# --- Button Row with External Links ---
st.markdown("<br>", unsafe_allow_html=True)
btn_cols = st.columns([1, 0.05, 1, 0.05, 1])
for i, sat in enumerate(satellite_data):
    with btn_cols[i * 2]:
        st.markdown(f"""
            <a href="{sat['url']}" target="_blank">
                <button class="sat-btn">{sat['button_label']}</button>
            </a>
        """, unsafe_allow_html=True)

# --- Spacer before Bottom Border ---
st.markdown("<div style='margin-top: 60px;'></div>", unsafe_allow_html=True)

# --- Bottom Border Image ---
bot_col1, bot_col2, bot_col3 = st.columns([1, 3, 1])
with bot_col2:
    st.image("images/border.png", width=4000)
