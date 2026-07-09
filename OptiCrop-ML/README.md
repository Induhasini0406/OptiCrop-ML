# OptiCrop – Smart Agricultural Production Optimization Engine

OptiCrop is a complete, production-quality Machine Learning web application designed to optimize agricultural output. By utilizing an ensemble **Random Forest Classifier** model trained on extensive crop-soil data, OptiCrop predicts the most suitable crop to cultivate based on seven critical chemical and environmental indicators.

---

## 🌟 Features

- **ML Inference Engine**: Loads pre-trained ensemble model (`RandomForestClassifier`) to perform sub-millisecond predictions.
- **Strict Multi-tier Validation**: Checks inputs on both client-side (real-time error checking, validation styling, boundaries alerts) and server-side to reject empty/non-numeric values.
- **Sophisticated Responsive UI**: A premium, mobile-optimized agriculture theme utilizing HSL tailored forest greens, elegant cards, and clear typography.
- **Glassmorphism Design**: Frosted glass elements (`backdrop-filter`) and smooth transition effects create a premium dashboard feel.
- **Diagnostic Summaries**: Returns prediction outputs with dynamic confidence percentages and interactive indicator audits.
- **Detailed About Portal**: Explains the technical machine learning training, normalization, and inference steps.

---

## 🛠️ Tech Stack

- **Backend Core**: Python 3, Flask 3.0+
- **Data Science/ML**: Scikit-learn, Numpy, Pickle
- **Frontend Presentation**: HTML5, Vanilla CSS3, Bootstrap 5, FontAwesome Icons
- **Dynamic Interactions**: Vanilla JavaScript (ES6)

---

## 📁 Folder Structure

```
OptiCrop/
├── app.py                  # Main Flask backend server and input validator
├── requirements.txt        # Backend python dependencies
├── README.md               # Project documentation
├── model/
│   ├── crop_model.pkl      # Pre-trained RandomForestClassifier model
│   └── label_encoder.pkl   # Fit label decoder for class outputs mapping
├── templates/
│   ├── base.html           # Core layout page wrapper (Navbar, Footer, CSS/JS inclusions)
│   ├── index.html          # Form entry page with client-side verification
│   ├── result.html         # Optimization output page with diagnostic summary
│   ├── about.html          # Explanatory scientific methodology page
│   └── error.html          # Validation failure & fault resolution display page
└── static/
    ├── css/
    │   └── style.css       # Premium custom stylesheet (green palettes, glassmorphism, animations)
    ├── js/
    │   └── app.js          # Forms verification, errors rendering, and loader control
    └── images/             # Background assets or banners
```

---

## ⚙️ Installation & Setup

### 1. Prerequisites
Make sure **Python 3.8+** is installed on your local computer.

### 2. Install Dependencies
Run the command below in your terminal inside the project root directory:
```bash
pip install -r requirements.txt
```

---

## 🚀 How to Run

Run the Flask server:
```bash
python app.py
```
By default, the server runs in developer mode and is accessible at:
[http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## 📊 Evaluation Metrics & Input Ranges

To test the application, you can input values matching standard soil profiles. Below are standard optimal ranges checked by our engine:

| Metric | Target Metric | Realistic Boundary Limits | Test Case (Rice) |
| :--- | :--- | :--- | :--- |
| **N** | Soil Nitrogen | 0.0 - 150.0 kg/ha | **90.0** |
| **P** | Soil Phosphorus | 5.0 - 150.0 kg/ha | **42.0** |
| **K** | Soil Potassium | 5.0 - 210.0 kg/ha | **43.0** |
| **pH** | Soil Acidity | 3.5 - 9.0 | **6.5** |
| **Temp** | Ambient Temperature | 0.0 - 50.0 °C | **20.87** |
| **Humidity** | Air Humidity | 10.0 - 100.0% | **82.0** |
| **Rainfall** | Precipitation | 20.0 - 300.0 mm | **202.93** |

---

## 📸 Screenshots Placeholder

*Insert UI Screenshots here:*
- **Home Dashboard**: Input forms with responsive cards.
- **Success Result Card**: Animated prediction badges and confidence parameters breakdown.
- **Error Validation Display**: Bulleted error feedback messages for inputs violating bounds.

---

## 🔮 Future Improvements

1. **API Endpoints Expansion**: Allow batch inputs JSON uploads for prediction.
2. **Weather API Integration**: Automatically pull real-time location temperature, humidity, and rainfall based on coordinates.
3. **Database Caching**: Store prediction requests history to analyze geographic optimization requests over time.
"# OptiCrop-ML" 
"# OptiCrop-ML" 
