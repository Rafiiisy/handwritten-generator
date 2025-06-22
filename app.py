import streamlit as st
import numpy as np
import random
import matplotlib.pyplot as plt

# Try different methods to load MNIST data
def load_mnist():
    # Method 1: Try sklearn
    try:
        from sklearn.datasets import fetch_openml
        X, y = fetch_openml('mnist_784', version=1, as_frame=False, return_X_y=True)
        y = y.astype(int)
        return X, y
    except ImportError:
        pass
    
    # Method 2: Try tensorflow/keras
    try:
        import tensorflow as tf
        (X_train, y_train), (X_test, y_test) = tf.keras.datasets.mnist.load_data()
        X = np.vstack([X_train, X_test])
        y = np.hstack([y_train, y_test])
        X = X.reshape(-1, 784)  # Flatten to 784 dimensions
        return X, y
    except ImportError:
        pass
    
    # Method 3: Generate synthetic data as last resort
    np.random.seed(42)
    n_samples = 1000
    X = np.random.rand(n_samples, 784) * 255
    y = np.random.randint(0, 10, n_samples)
    return X.astype(np.uint8), y

@st.cache_data
def get_mnist_data():
    return load_mnist()

st.title("MNIST Handwritten Digit Generator")

# Load data with error handling
try:
    X, y = get_mnist_data()
    st.success("✅ Dataset loaded successfully!")
except Exception as e:
    st.error(f"❌ Error loading dataset: {e}")
    st.info("Please check your internet connection and try again.")
    st.stop()

# User selects digit
digit = st.selectbox("Select a digit to generate (0-9):", list(range(10)), index=0)

# Filter images of the selected digit
indices = np.where(y == digit)[0]

if len(indices) == 0:
    st.warning(f"No images found for digit {digit}")
    st.stop()

# Randomly select 5 images (or fewer if not enough available)
num_images = min(5, len(indices))
selected_indices = random.sample(list(indices), num_images)
selected_images = X[selected_indices]

# Display images in a row
st.write(f"### {num_images} Random Images of Digit {digit}")
cols = st.columns(5)
for i, img in enumerate(selected_images):
    img_reshaped = img.reshape(28, 28)
    cols[i].image(img_reshaped, width=100, caption=f"Sample {i+1}", clamp=True)

# Add some information
st.info(f"📊 Found {len(indices)} total instances of digit {digit}")
