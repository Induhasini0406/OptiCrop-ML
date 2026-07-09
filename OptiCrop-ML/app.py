import os
import pickle
import warnings
import numpy as np
from flask import Flask, render_template, request, redirect, url_for

# Suppress unpickle and feature names warnings from sklearn
warnings.filterwarnings("ignore", category=UserWarning)

app = Flask(__name__)

# Load model and label encoder once at startup
MODEL_PATH = os.path.join("model", "crop_model.pkl")
ENCODER_PATH = os.path.join("model", "label_encoder.pkl")

model = None
label_encoder = None

try:
    with open(MODEL_PATH, "rb") as f:
        model = pickle.load(f)
    with open(ENCODER_PATH, "rb") as f:
        label_encoder = pickle.load(f)
    print("Model and Label Encoder successfully loaded.")
except Exception as e:
    print(f"Error loading models at startup: {e}")

# Validate inputs helper
def validate_inputs(form):
    errors = []
    
    # 7 Required features
    fields = {
        'N': ('Nitrogen', 0.0, 150.0),
        'P': ('Phosphorus', 5.0, 150.0),
        'K': ('Potassium', 5.0, 210.0),
        'temperature': ('Temperature', 0.0, 50.0),
        'humidity': ('Humidity', 10.0, 100.0),
        'ph': ('pH Level', 3.5, 9.0),
        'rainfall': ('Rainfall', 20.0, 300.0)
    }
    
    validated_values = {}
    
    for key, (label, min_val, max_val) in fields.items():
        val = form.get(key)
        
        # Empty Check
        if val is None or val.strip() == '':
            errors.append(f"{label} is required and cannot be empty.")
            continue
            
        # Numeric Check
        try:
            val_f = float(val)
        except ValueError:
            errors.append(f"{label} must be a valid numeric value.")
            continue
            
        # Range Check (standard agriculture bounds)
        if val_f < min_val or val_f > max_val:
            errors.append(f"{label} must be within realistic bounds ({min_val} to {max_val}).")
            continue
            
        validated_values[key] = val_f
        
    return errors, validated_values

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if model is None or label_encoder is None:
        return render_template('error.html', errors=["Model or Label Encoder was not initialized properly. Please check backend logs."])
        
    try:
        errors, val_data = validate_inputs(request.form)
        
        if errors:
            # If validation fails, render error template with specific errors
            return render_template('error.html', errors=errors)
            
        # Prepare feature vector in exact order: [N, P, K, temp, hum, ph, rain]
        features = [
            val_data['N'],
            val_data['P'],
            val_data['K'],
            val_data['temperature'],
            val_data['humidity'],
            val_data['ph'],
            val_data['rainfall']
        ]
        
        # Convert to numpy array and reshape for prediction
        features_arr = np.array([features])
        
        # Make prediction
        pred_idx = model.predict(features_arr)[0]
        
        # Decode predicted class index to crop name
        crop_name = label_encoder.inverse_transform([pred_idx])[0]
        # Capitalize for UI
        crop_name_display = crop_name.capitalize()
        
        # Calculate confidence if model supports it
        confidence = None
        if hasattr(model, "predict_proba"):
            proba = model.predict_proba(features_arr)[0]
            confidence = round(float(np.max(proba) * 100), 2)
            
        # Map crop names to emojis for bonus visual appeal
        crop_emojis = {
            'rice': '🌾',
            'maize': '🌽',
            'chickpea': '🌱',
            'kidneybeans': '🫘',
            'pigeonpeas': '🪴',
            'mothbeans': '🌿',
            'mungbean': '🥗',
            'blackgram': '🍲',
            'lentil': '🥣',
            'pomegranate': '🍎',
            'banana': '🍌',
            'mango': '🥭',
            'grapes': '🍇',
            'watermelon': '🍉',
            'muskmelon': '🍈',
            'apple': '🍎',
            'orange': '🍊',
            'papaya': '🥭',
            'coconut': '🥥',
            'cotton': '☁️',
            'jute': '🧵',
            'coffee': '☕'
        }
        
        emoji = crop_emojis.get(crop_name.lower(), '🌱')
        
        return render_template(
            'result.html', 
            crop=crop_name_display, 
            confidence=confidence, 
            emoji=emoji,
            inputs=val_data
        )
        
    except Exception as e:
        app.logger.error(f"Prediction error: {e}")
        return render_template('error.html', errors=[f"An unexpected error occurred during prediction: {str(e)}"])

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    # Running locally in dev mode
    app.run(debug=True, host='0.0.0.0', port=5000)
