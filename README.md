# ✏️ Handwritten Digit Generator

A beautiful Streamlit web application that generates and displays handwritten digits from the MNIST dataset.

## 🚀 Features

- **Random Digit Generator**: Generate random handwritten digits
- **Specific Digit Viewer**: View specific digits (0-9)
- **Multiple Digits Display**: Show multiple digits in various modes
- **Dataset Information**: View detailed statistics about the MNIST dataset
- **Beautiful UI**: Modern, responsive design with custom styling

## 📦 Installation

### Local Development

1. **Clone the repository**
   ```bash
   git clone https://github.com/Rafiiisy/handwritten-generator.git
   cd handwritten-generator
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**
   ```bash
   streamlit run streamlit_app.py
   ```

4. **Open your browser**
   Navigate to `http://localhost:8501`

## 🌐 Deployment Options

### Option 1: Streamlit Cloud (Recommended)

1. **Push to GitHub**
   ```bash
   git add .
   git commit -m "Initial commit"
   git push origin main
   ```

2. **Deploy on Streamlit Cloud**
   - Go to [share.streamlit.io](https://share.streamlit.io)
   - Sign in with GitHub
   - Click "New app"
   - Select your repository: `Rafiiisy/handwritten-generator`
   - Set the main file path: `streamlit_app.py`
   - Click "Deploy"

### Option 2: Heroku

1. **Create Procfile**
   ```
   web: streamlit run streamlit_app.py --server.port=$PORT --server.address=0.0.0.0
   ```

2. **Create runtime.txt**
   ```
   python-3.9.16
   ```

3. **Deploy to Heroku**
   ```bash
   heroku create your-app-name
   git push heroku main
   ```

### Option 3: Railway

1. **Connect your GitHub repository**
2. **Set build command**: `pip install -r requirements.txt`
3. **Set start command**: `streamlit run streamlit_app.py --server.port=$PORT --server.address=0.0.0.0`

## 📁 Project Structure

```
handwritten-generator/
├── streamlit_app.py      # Main Streamlit application
├── app.py               # Original simple version
├── requirements.txt     # Python dependencies
├── README.md           # This file
└── .gitignore          # Git ignore file
```

## 🛠️ Dependencies

- `streamlit==1.28.1` - Web framework
- `scikit-learn==1.3.0` - Machine learning library (for MNIST dataset)
- `numpy==1.24.3` - Numerical computing
- `matplotlib==3.7.2` - Plotting library
- `pandas==2.0.3` - Data manipulation

## 🎯 Usage

1. **Random Digit Generation**
   - Click "🎲 Generate Random Digit" to see a random handwritten digit

2. **Specific Digit Viewing**
   - Select a digit (0-9) from the dropdown
   - Click "🔍 Show Digit" to view a random instance of that digit

3. **Multiple Digits Display**
   - Choose the number of digits to display
   - Select display mode:
     - **Random digits**: Random selection from all digits
     - **One of each digit**: One instance of each digit (0-9)
     - **Specific digit only**: Multiple instances of a chosen digit
   - Click "🖼️ Generate Display" to show the results

## 📊 Dataset Information

The application uses the **MNIST dataset** which contains:
- **70,000** handwritten digit images
- **28x28** pixel grayscale images
- **10** classes (digits 0-9)
- Balanced distribution across all digits

## 🔧 Customization

### Adding New Features

1. **New Display Modes**: Add options to the `display_mode` selectbox
2. **Custom Styling**: Modify the CSS in the `st.markdown` section
3. **Additional Datasets**: Extend the `load_mnist()` function

### Styling

The app uses custom CSS for styling. You can modify the styles in the `st.markdown` section at the top of `streamlit_app.py`.

## 🐛 Troubleshooting

### Common Issues

1. **Import Errors**
   ```bash
   pip install --upgrade streamlit scikit-learn
   ```

2. **Dataset Loading Issues**
   - Check your internet connection
   - The MNIST dataset will be downloaded automatically on first run

3. **Display Issues**
   - Ensure matplotlib is properly installed
   - Try refreshing the browser

### Git Issues

If you encounter git push issues:

```bash
# Initialize git if not already done
git init

# Add your remote origin
git remote add origin https://github.com/Rafiiisy/handwritten-generator.git

# Create and switch to main branch
git checkout -b main

# Add and commit files
git add .
git commit -m "Initial commit"

# Push to GitHub
git push -u origin main
```

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## 📞 Support

If you encounter any issues or have questions:
- Open an issue on GitHub
- Check the Streamlit documentation: [docs.streamlit.io](https://docs.streamlit.io)

---

**Happy coding! 🚀**
