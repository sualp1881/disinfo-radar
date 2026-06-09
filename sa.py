import streamlit as st
import librosa
import librosa.display
import matplotlib.pyplot as plt
import numpy as np

# Arayüz ayarları
st.set_page_config(page_title="Disinformation Radar", layout="wide")
st.title("🛡️ Disinformation Radar: Audio Analysis Tool")
st.markdown("---")
st.write("This tool analyzes audio files to detect frequency anomalies and potential AI-generated voice content.")

# Dosya yükleme (İngilizce)
st.sidebar.header("Upload File")
uploaded_file = st.sidebar.file_uploader("Select a .wav file for analysis", type=["wav"])

if uploaded_file is not None:
    with st.spinner('Analyzing the audio...'):
        # Ses dosyası yükleme
        y, sr = librosa.load(uploaded_file, sr=None)
        
        # Spektrogram analizi
        mel_spectrogram = librosa.feature.melspectrogram(y=y, sr=sr, n_mels=128)
        mel_spectrogram_db = librosa.power_to_db(mel_spectrogram, ref=np.max)
        
        # Görselleştirme
        fig, ax = plt.subplots(figsize=(10, 4))
        img = librosa.display.specshow(mel_spectrogram_db, sr=sr, x_axis='time', y_axis='mel', ax=ax)
        fig.colorbar(img, ax=ax, format='%+2.0f dB')
        ax.set_title('Mel-Spectrogram Analysis')
        
        # Sonuç mesajı
        st.success("Analysis complete!")
        st.pyplot(fig)
        
        # Teknik not
        st.info("Technical Note: The map above shows the frequency distribution. AI-generated voices often exhibit highly regular frequency patterns.")
else:
    st.warning("Please upload a .wav file from the sidebar to begin.")