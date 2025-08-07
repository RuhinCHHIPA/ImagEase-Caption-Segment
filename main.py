import streamlit as st
from PIL import Image
import os
import sys
from io import BytesIO
import zipfile

# Add your core folder to path
sys.path.append(os.path.abspath("core"))
from core.captioning import generate_caption
from core.segmentation import generate_segmentation

# Page config
st.set_page_config(page_title="imagEase", layout="centered")

# Page routing setup
if 'page' not in st.session_state:
    st.session_state.page = 'home'

def go_to(page_name):
    st.session_state.page = page_name

# =================== GLOBAL CSS ===================
st.markdown("""
    <style>
    html, body, [data-testid="stAppViewContainer"] {
        background-color: #fff9f0;
    }
    body {
        background: linear-gradient(135deg, #fff0c1, #ffd6e0);
        font-family: 'Segoe UI', sans-serif;
        color: #333333;
        animation: gradientAnimation 15s ease infinite; 
    }
    @keyframes gradientAnimation {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }
    .main {
        background: linear-gradient(135deg, #FFEFBA, #FFFFFF);
        background-attachment: fixed;   
        background-color: #ffffff;
        padding: 2rem;
        border-radius: 15px;
        box-shadow: 0px 4px 20px rgba(0, 0, 0, 0.1);
        margin: 2rem auto;
        max-width: 800px;
    }
    .login-heading {
        font-size: 2.8em;
        font-weight: bold;
        color: #ff4b4b;
        text-align: center;
        margin-bottom: 0.5em;
    }
    .login-subheading {
        font-size: 1.2em;
        text-align: center;
        color: #444;
        margin-bottom: 2em;
    }
    .stButton button {
        background: linear-gradient(to right, #ff6a00, #ee0979);
        color: white !important;
        border: none;
        padding: 0.75em 1.5em;
        font-size: 1em;
        font-weight: bold;
        border-radius: 25px;
        cursor: pointer;
        transition: transform 0.2s ease-in-out;
    }
    .stButton button:hover {
        transform: scale(1.05);
        background: linear-gradient(to right, #ee0979, #ff6a00);
    }
    .image-frame {
        border: 6px solid #f8b500;
        border-radius: 20px;
        box-shadow: 0 8px 20px rgba(0, 0, 0, 0.2);
        padding: 10px;
        background-color: #fffbe6;
        margin: 20px auto;
        width: fit-content;
    }
    .caption-box {
        background-color: #f0f8ff;
        border-left: 5px solid #0066cc;
        padding: 15px;
        margin-top: 20px;
        border-radius: 8px;
        box-shadow: 0 2px 5px rgba(0,0,0,0.1);
        font-size: 16px;
        line-height: 1.6;
    }
    </style>
""", unsafe_allow_html=True)

# ===================== HOME =====================
if st.session_state.page == 'home':
    st.markdown("""
    <div class="main">
        <h1 class="login-heading">🌟 Welcome to <span style='color: #0066cc;'>imagEase</span> 📸</h1>
         <p class="project-desc">
        💡 <strong>imagEase</strong> is an AI-powered tool that automatically:<br>
        🧩 Segments images with pixel-level precision<br>
        ✍️ Generates intelligent, human-like captions<br>
        ⚡ Helps you understand visuals faster and better.
    </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <style>
    .confetti-piece {
        width: 10px;
        height: 10px;
        background-color: #f2a365;
        position: fixed;
        top: -10px;
        animation: fall 5s linear infinite;
        opacity: 0.8;
        z-index: 9999;
    }

    .confetti-piece:nth-child(1) { left: 10%; animation-delay: 0s; background-color: #f38181; }
    .confetti-piece:nth-child(2) { left: 20%; animation-delay: 0.5s; background-color: #fce38a; }
    .confetti-piece:nth-child(3) { left: 30%; animation-delay: 1s; background-color: #eaffd0; }
    .confetti-piece:nth-child(4) { left: 40%; animation-delay: 1.5s; background-color: #95e1d3; }
    .confetti-piece:nth-child(5) { left: 50%; animation-delay: 2s; background-color: #fcd1d1; }
    .confetti-piece:nth-child(6) { left: 60%; animation-delay: 2.5s; background-color: #c4fae8; }
    .confetti-piece:nth-child(7) { left: 70%; animation-delay: 3s; background-color: #c5a3ff; }
    .confetti-piece:nth-child(8) { left: 80%; animation-delay: 3.5s; background-color: #f38181; }
    .confetti-piece:nth-child(9) { left: 90%; animation-delay: 4s; background-color: #fce38a; }

    @keyframes fall {
        0% {
            transform: translateY(0) rotate(0deg);
            opacity: 1;
        }
        100% {
            transform: translateY(100vh) rotate(720deg);
            opacity: 0;
        }
    }
    </style>

    <div class="confetti-piece"></div>
    <div class="confetti-piece"></div>
    <div class="confetti-piece"></div>
    <div class="confetti-piece"></div>
    <div class="confetti-piece"></div>
    <div class="confetti-piece"></div>
    <div class="confetti-piece"></div>
    <div class="confetti-piece"></div>
    <div class="confetti-piece"></div>
    """, unsafe_allow_html=True)

    if st.button("🎨 Let's Begin → Caption & Segment 🧠"):
        go_to('caption')


# ================== CAPTION & SEGMENT PAGE ==================
elif st.session_state.page == 'caption':
    st.markdown("""
    <div class="main">
        <h1 class="login-heading" style="color: #0066cc;">🎬 imagEase 🎨</h1>
        <p class="login-subheading">
            Upload your custom image 🖼️ or select a demo example from the gallery below 📂.<br>
            Then, let AI ✨ generate smart captions ✍️ and highlight objects via segmentation 🔍.
        </p>
    </div>
    """, unsafe_allow_html=True)

    uploaded_file = st.file_uploader("📤 Upload your image", type=["jpg", "jpeg", "png"])

    demo_folder = "demo_images"
    demo_images = [img for img in os.listdir(demo_folder) if img.lower().endswith(('.jpg', '.jpeg', '.png'))]
    selected_image_name = st.selectbox("🖼️ Or, choose a Demo Image", ["-- Select --"] + demo_images)

    st.markdown("### 🔍 Image Preview")
    image = None
    image_source = None

    if uploaded_file is not None:
        image = Image.open(uploaded_file).convert("RGB")
        st.markdown('<div class="image-frame">', unsafe_allow_html=True)
        st.image(image, caption="📷 Your Uploaded Image", use_container_width=False, width=400)
        st.markdown('</div>', unsafe_allow_html=True)
        image_source = uploaded_file

    elif selected_image_name != "-- Select --":
        image_path = os.path.join(demo_folder, selected_image_name)
        if os.path.exists(image_path):
            image = Image.open(image_path).convert("RGB")
            st.markdown('<div class="image-frame">', unsafe_allow_html=True)
            st.image(image, caption=f"🖼️ Demo Image: {selected_image_name}", use_container_width=False, width=400)
            st.markdown('</div>', unsafe_allow_html=True)
            image_source = image_path
        else:
            st.error("❌ Selected image not found. Please check filename or path.")

    if image_source:
        col1, col2 = st.columns(2)

        with col1:
            if st.button("📝 Generate Caption ✍️"):
                with st.spinner("AI is writing your image story..."):
                    caption = generate_caption(image_source)

                    # Styled caption display
                    st.markdown(f"<div class='caption-box'>🗨️ <strong>Generated Caption:</strong><br>{caption}</div>", unsafe_allow_html=True)

                    # Save image in memory
                    img_bytes = BytesIO()
                    if isinstance(image_source, str):
                        image = Image.open(image_source).convert("RGB")
                    elif hasattr(image_source, 'read'):
                        image = Image.open(image_source).convert("RGB")
                    image.save(img_bytes, format='JPEG')
                    img_bytes.seek(0)

                    # Create ZIP file
                    zip_buffer = BytesIO()
                    with zipfile.ZipFile(zip_buffer, "w", zipfile.ZIP_DEFLATED) as zip_file:
                        zip_file.writestr("caption.txt", caption)
                        zip_file.writestr("image.jpg", img_bytes.getvalue())
                    zip_buffer.seek(0)

                    st.download_button(
                        label="📥 Download Caption + Image (ZIP)",
                        data=zip_buffer,
                        file_name="caption_with_image.zip",
                        mime="application/zip"
                    )

        with col2:
            if st.button("🧩 Segment Image 🎯"):
                with st.spinner("Detecting objects with precision..."):
                    segmented_img = generate_segmentation(image_source)
                    st.markdown('<div class="image-frame">', unsafe_allow_html=True)
                    st.image(segmented_img, caption="🎨 Segmented Output", use_container_width=True)
                    st.markdown('</div>', unsafe_allow_html=True)

                    buffer = BytesIO()
                    segmented_img.save(buffer, format="PNG")
                    st.download_button(
                        label="📥 Download Segmented Image (.png)",
                        data=buffer.getvalue(),
                        file_name="segmented_output.png",
                        mime="image/png"
                    )

    if st.button("📖 Go to About →"):
        go_to('about')

# =================== ABOUT PAGE ====================
elif st.session_state.page == "about":
    import About
    About.app()
