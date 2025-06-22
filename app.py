import streamlit as st
import numpy as np
from sklearn.datasets import fetch_openml
import random
import matplotlib.pyplot as plt

st.title("MNIST Handwritten Digit Generator")

# Load MNIST dataset (only once)
@st.cache_data
def load_mnist():
    X, y = fetch_openml('mnist_784', version=1, as_frame=False, return_X_y=True)
    y = y.astype(int)
    return X, y

X, y = load_mnist()

# User selects digit
digit = st.selectbox("Select a digit to generate (0-9):", list(range(10)), index=0)

# Filter images of the selected digit
indices = np.where(y == digit)[0]

# Randomly select 5 images
selected_indices = random.sample(list(indices), 5)
selected_images = X[selected_indices]

# Display images in a row
st.write(f"### 5 Random Images of Digit {digit}")
cols = st.columns(5)
for i, img in enumerate(selected_images):
    img_reshaped = img.reshape(28, 28)
    cols[i].image(img_reshaped, width=100, caption=f"Sample {i+1}", clamp=True)
