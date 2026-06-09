import os

# GitHub'a kütüphaneleri requirements.txt olmadan tanıtalım
os.system("pip install streamlit librosa matplotlib numpy")

import streamlit as st
import librosa
import librosa.display
import matplotlib.pyplot as plt
import numpy as np

st.set_page_config(page_title="Disinformation Radar", layout="wide")
st.title("🛡️ Disinformation Radar: Audio Analysis Tool")
st.markdown("---")
# ... (kodun geri kalanı aynı)
