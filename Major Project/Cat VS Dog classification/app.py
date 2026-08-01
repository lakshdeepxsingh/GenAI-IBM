import streamlit as st
import tensorflow as tf
from tensorflow.keras.preprocessing import image
import numpy as np

# ---------------- PAGE CONFIG ----------------

st.set_page_config(
    page_title="Cat vs Dog Classifier",
    page_icon="🐱",
    layout="centered"
)

# ---------------- LOAD MODEL ----------------

from tensorflow.keras.models import load_model

@st.cache_resource
def load_my_model():
    return load_model("model/cat_dog_model.keras")

model = load_my_model()

st.markdown("""
<style>

/* Main Background */
.stApp{
    background: linear-gradient(135deg,#0f172a,#1e293b,#111827);
}

/* Hide Streamlit elements */
#MainMenu {visibility:hidden;}
footer {visibility:hidden;}
header {visibility:hidden;}

/* Title */
.title{
    text-align:center;
    font-size:56px;
    font-weight:800;
    color:white;
}

/* Subtitle */
.subtitle{
    text-align:center;
    color:#cbd5e1;
    font-size:20px;
    margin-bottom:35px;
}

/* Upload Box */
div[data-testid="stFileUploader"]{
    background:white;
    border:2px dashed #3b82f6;
    border-radius:18px;
    padding:22px;
    box-shadow:0px 8px 25px rgba(0,0,0,0.25);
}

/* Uploaded image */
img{
    border-radius:18px;
}

/* Prediction Card */
.prediction-card{
    background:#1e293b;
    padding:25px;
    border-radius:18px;
    border:1px solid #334155;
    text-align:center;
    margin-top:25px;
    box-shadow:0px 0px 25px rgba(59,130,246,.25);
}

/* Footer */
.footer{
    text-align:center;
    color:#94a3b8;
    margin-top:35px;
    font-size:17px;
}

</style>
""", unsafe_allow_html=True)

# ---------------- TITLE ----------------

st.markdown("<div class='main-box'>", unsafe_allow_html=True)

st.markdown("<div class='title'>🐱 Cat vs Dog Classifier 🐶</div>", unsafe_allow_html=True)

st.markdown(
"<div class='subtitle'>Upload an image and let the AI predict whether it is a Cat or a Dog.</div>",
unsafe_allow_html=True
)

# ---------------- FILE UPLOADER ----------------

uploaded_file = st.file_uploader(
    "📤 Upload an Image",
    type=["jpg","jpeg","png"]
)

# ---------------- PREDICTION ----------------

if uploaded_file is not None:

    from PIL import Image

    display_img = Image.open(uploaded_file)
    display_img = display_img.resize((320, 320))

    col1, col2, col3 = st.columns([1,2,1])

    with col2:
        st.image(
            display_img,
            caption="Uploaded Image",
            width=320
        )

    img = image.load_img(uploaded_file, target_size=(150,150))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = img_array / 255.0

    prediction = model.predict(img_array)[0][0]

    confidence = prediction if prediction > 0.5 else (1-prediction)
    confidence = confidence * 100

    if prediction > 0.5:
        animal = "🐶 DOG"
        color = "#dbeafe"
    else:
        animal = "🐱 CAT"
        color = "#dcfce7"

    st.markdown(
        f"""
        <div style="
        background:{color};
        padding:25px;
        border-radius:18px;
        margin-top:25px;
        box-shadow:0px 5px 15px rgba(0,0,0,0.12);
        text-align:center;
        ">
        <h2>{animal}</h2>
        <h4>Confidence: {confidence:.2f}%</h4>
        </div>
        """,
        unsafe_allow_html=True
    )

else:
    st.info("👆 Upload a JPG or PNG image to classify it.")

st.markdown(
"<div class='footer'>💙 Built with TensorFlow & Streamlit</div>",
unsafe_allow_html=True
)

st.markdown("</div>", unsafe_allow_html=True)