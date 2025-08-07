import streamlit as st

def app():
    st.markdown("""
    <style>
    .about-section {
        background: linear-gradient(135deg, #fff0f5, #e6f7ff);
        padding: 40px 60px;
        border-radius: 20px;
        font-family: 'Segoe UI', sans-serif;
        color: #333;
        box-shadow: 0 10px 25px rgba(0,0,0,0.15);
        margin-top: 30px;
    }
    .about-section h1 {
        color: #ff4b4b;
        font-size: 2.8em;
        text-align: center;
        margin-bottom: 10px;
    }
    .about-section h2 {
        color: #ff8800;
        font-size: 1.7em;
        margin-top: 25px;
    }
    .about-section p {
        font-size: 1.15em;
        line-height: 1.8;
        margin-bottom: 10px;
    }
    .about-section ul {
        font-size: 1.1em;
        line-height: 1.8;
        padding-left: 20px;
    }
    .about-section li {
        margin-bottom: 8px;
    }
    </style>

    <div class="about-section">

    <h1>📖 About <span style='color:#ff8800;'>ImagEase</span></h1>

    <p>✨ <b>ImagEase</b> is a powerful, beginner-friendly AI tool that lets you:</p>

    <ul>
        <li>📝 Generate smart captions for any image</li>
        <li>🧩 Segment & highlight objects inside images</li>
        <li>📂 Use your own images or test with built-in demos</li>
        <li>📥 Download captioned and segmented results easily</li>
    </ul>

    <h2>🚀 How It Works</h2>
    <ul>
        <li>1️⃣ Upload or select an image 📤</li>
        <li>2️⃣ Click on either caption or segment buttons 🎯</li>
        <li>3️⃣ Instantly see & download results 💡</li>
    </ul>

    <h2>⚙️ Built With</h2>
    <ul>
        <li>🌐 <b>Streamlit</b> – For the web interface</li>
        <li>🤖 <b>HuggingFace BLIP</b> – For captioning</li>
        <li>🎯 <b>Mask R-CNN</b> – For object segmentation</li>
        <li>🖼️ <b>Pillow (PIL)</b> – For image rendering</li>
        <li>📒 <b>Jupyter Notebook</b> – For model testing</li>
    </ul>

    <h2>💡 Made By</h2>
    <p>
        👩‍💻 <b>Ruhin Chhipa</b><br>
        🏫 BSc IT (Dual), GLS University<br>
        💼 Developed as part of Zidio Internship 2025
    </p>

    </div>
    """, unsafe_allow_html=True)
