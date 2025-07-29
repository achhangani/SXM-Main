import streamlit as st
from PIL import Image
import random
from pathlib import Path

# --- UI Cleanup ---
st.markdown(""" <style> #MainMenu {visibility: hidden;} footer {visibility: hidden;} header {visibility: hidden;} </style> """, unsafe_allow_html=True)

# --- Cosmic Top & Bottom Accent ---
st.markdown("""
<style>
.cosmic-top, .cosmic-bottom {
    position: fixed;
    width: 100%;
    text-align: center;
    font-size: 22px;
    color: #ffffff;
    padding: 6px 0px;
    z-index: 9999;
    background-color: transparent;
    pointer-events: none;
}
.cosmic-top { top: 0; right: 0; left: 0; }
.cosmic-bottom { bottom: 0;right: 0; left: 0; }
</style>

<div class='cosmic-top'>
🌠🛰️🌌🔭✨📡🪐🎧🌍💫🎶🚀🎙️🌐🌟🛸🔊🌙🔮📻
</div>
<div class='cosmic-bottom'>
📡🚀🌠💫🌍🎶🎧🔭🪐✨🌌🌟🔊🛸🎙️🌙🔮📻🛰️🌟
</div>
""", unsafe_allow_html=True)

# --- Layout Tweak ---
st.markdown("""
<style>
.block-container {
    padding-top: 20px;
    margin-top: -40px;
}
</style>
""", unsafe_allow_html=True)

# --- Vertical Borders ---
st.markdown("""
<style>
.emoji-vertical {
  writing-mode: vertical-rl;
  position: fixed;
  top: 0;
  height: 100vh;
  font-size: 23px;
  color: white;
  font-weight: bold;
  padding: 4px;
  z-index: 1000;
}
.emoji-left { left: 0; }
.emoji-right { right: 0; }
</style>

<div class="emoji-vertical emoji-left">
🚀🌌🎧🎙️🛰️📡💫🌍🎧🔭🪐🌚🗼📻✨🔊🌟🎶🛸
</div>
<div class="emoji-vertical emoji-right">
🌚🪐🎧🔊🌠🛰️🌍📻🗼🎵✨🎶🌟💫🔭🎙️🚀🛸📡
</div>
""", unsafe_allow_html=True)

# --- Page Setup ---
st.set_page_config(page_title="🛰️ SXM Satellite Directory", layout="wide")

# --- Styling ---
st.markdown("""
<style>
[data-testid="stSidebar"] { display: none; }
body {
    background-image: url("https://i.imgur.com/tLJUZFt.png");
    background-size: cover;
    background-attachment: fixed;
}
h1, h3 { color: #ffffff; }
.station-badge {
    font-size: 13px;
    font-weight: bold;
    color: #fff;
    background-color: #4b3895;
    padding: 5px 12px;
    border-radius: 16px;
    font-family: 'Courier New', Courier, monospace;
}
.stream-visual {
    font-size: 18px;
    color: #c9c3ff;
    margin-top: 2px;
    font-family: 'Courier New', Courier, monospace;
}
.sat-btn {
    background: linear-gradient(135deg, #d5cfff, #e0d8f9);
    border: none;
    color: #4b3895;
    padding: 12px 20px;
    border-radius: 8px;
    font-weight: bold;
    font-size: 15px;
    width: 100%;
    cursor: pointer;
    box-shadow: 0 2px 6px rgba(0,0,0,0.15);
}
.sat-btn:hover {
    background: linear-gradient(135deg, #c3b5f3, #d5cfff);
}
.space-icon {
    position: absolute;
    font-size: 22px;
    color: #ffffff88;
    z-index: 800;
}
</style>
""", unsafe_allow_html=True)

# --- Title ---
st.markdown("""
<div style='text-align:center; padding-top:0px;'>
    <h1 style='font-family:Georgia; font-size:32px;'>SXM Satellite Directory</h1>
    <h3 style='font-family:Georgia; font-size:18px;'>Choose your satellite below</h3>
</div>
""", unsafe_allow_html=True)

# --- Satellite Data with External URLs ---
satellite_data = [
    {
        "image_path": "images/satellite1.png",
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
