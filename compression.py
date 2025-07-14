import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from io import BytesIO

st.title('Compressione Immagine con Fourier 🐶📉')

file_upt = st.file_uploader('Carica una immagine', type=['jpg', 'jpeg', 'png'])

if file_upt is not None:

    image = Image.open(file_upt).convert('L')
    B = np.array(image)

    st.image(image, caption='Immagine originale', use_container_width=True)

    perct = st.slider("Percentuale di frequenze da conservare", 0.005, 0.5, 0.05, step=0.005)

    Bt = np.fft.fft2(B)
    Bt_abs_sorted = np.sort(np.abs(Bt.flatten()))

    tresh_index = int((1-perct) * len(Bt_abs_sorted))
    tresh = Bt_abs_sorted[tresh_index]

    mask = np.abs(Bt) > tresh
    Bt_low = Bt * mask

    Alow = np.fft.ifft2(Bt_low)
    Alow = np.abs(Alow).astype(np.uint8)

    st.subheader("Risultato dopo compressione")
    st.image(Alow, caption=f'Compressione con frequenze eliminate = {perct:.3f}', use_container_width=True)
