from flask import Flask, render_template, request, jsonify, session, redirect, url_for
import os
import numpy as np
from PIL import Image
import tensorflow as tf
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input
from werkzeug.utils import secure_filename
import secrets

app = Flask(__name__)
app.secret_key = secrets.token_hex(16)
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max file size
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['STATIC_FOLDER'] = 'static'

# Ensure folders exist
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
os.makedirs(os.path.join(app.config['STATIC_FOLDER'], 'images'), exist_ok=True)

# Load model
MODEL_PATH = "mobilenetv2_best.keras"
model = None
IMG_SIZE = (224, 224)
class_names = []

def load_model():
    global model, class_names
    try:
        model = tf.keras.models.load_model(MODEL_PATH)
        print(f"Model loaded successfully from {MODEL_PATH}")
        class_names = get_class_names()
    except Exception as e:
        print(f"Error loading model: {e}")

def get_class_names():
    # Replace with your actual class names
    return [
        'Apple___Apple_scab', 'Apple___Black_rot', 'Apple___Cedar_apple_rust',
        'Apple___healthy', 'Blueberry___healthy', 'Cherry_(including_sour)___Powdery_mildew',
        'Cherry_(including_sour)___healthy', 'Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot',
        'Corn_(maize)___Common_rust_', 'Corn_(maize)___Northern_Leaf_Blight',
        'Corn_(maize)___healthy', 'Grape___Black_rot', 'Grape___Esca_(Black_Measles)',
        'Grape___Leaf_blight_(Isariopsis_Leaf_Spot)', 'Grape___healthy',
        'Orange___Haunglongbing_(Citrus_greening)', 'Peach___Bacterial_spot',
        'Peach___healthy', 'Pepper,_bell___Bacterial_spot', 'Pepper,_bell___healthy',
        'Potato___Early_blight', 'Potato___Late_blight', 'Potato___healthy',
        'Raspberry___healthy', 'Soybean___healthy', 'Squash___Powdery_mildew',
        'Strawberry___Leaf_scorch', 'Strawberry___healthy', 'Tomato___Bacterial_spot',
        'Tomato___Early_blight', 'Tomato___Late_blight', 'Tomato___Leaf_Mold',
        'Tomato___Septoria_leaf_spot', 'Tomato___Spider_mites Two-spotted_spider_mite',
        'Tomato___Target_Spot', 'Tomato___Tomato_Yellow_Leaf_Curl_Virus',
        'Tomato___Tomato_mosaic_virus', 'Tomato___healthy'
    ]

def predict_image(img_path):
    img = Image.open(img_path).convert('RGB').resize(IMG_SIZE)
    arr = np.array(img).astype('float32')
    arr = preprocess_input(arr)
    arr = np.expand_dims(arr, axis=0)
    
    preds = model.predict(arr)[0]
    
    # Get top prediction index sorted by probability
    top_indices = preds.argsort()[-1:][::-1]
    
    results = []
    for idx in top_indices:
        results.append({
            'class': class_names[idx],
            'confidence': round(float(preds[idx]) * 100, 2)  # Convert to percentage and round
        })
    
    return results

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/upload')
def upload():
    return render_template('upload.html')

@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return jsonify({'error': 'No file uploaded'}), 400
    
    file = request.files['file']
    
    if file.filename == '':
        return jsonify({'error': 'No file selected'}), 400
    
    if file:
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        
        try:
            predictions = predict_image(filepath)
            
            # Save image to static folder for display
            static_filename = f"upload_{secrets.token_hex(8)}.jpg"
            static_path = os.path.join(app.config['STATIC_FOLDER'], 'images', static_filename)
            Image.open(filepath).save(static_path)
            
            # Store in session
            session['predictions'] = predictions
            session['image_path'] = f'images/{static_filename}'
            
            os.remove(filepath)  # Clean up temp file
            
            return jsonify({'success': True})
        except Exception as e:
            if os.path.exists(filepath):
                os.remove(filepath)
            return jsonify({'error': str(e)}), 500

@app.route('/result')
def result():
    predictions = session.get('predictions')
    image_path = session.get('image_path')
    
    if not predictions:
        return redirect(url_for('upload'))
        
    # Load disease info database
    disease_info = {}
    db_path = os.path.join(app.root_path, 'disease_info.json')
    if os.path.exists(db_path):
        import json
        with open(db_path, 'r') as f:
            disease_info = json.load(f)
            
    # Attach info to top prediction
    top_class = predictions[0]['class']
    info = disease_info.get(top_class, None)
    
    return render_template('result.html', predictions=predictions, image_path=image_path, info=info, all_classes=class_names)

@app.route('/feedback', methods=['POST'])
def feedback():
    try:
        data = request.json
        image_path = data.get('image_path')
        predicted_class = data.get('predicted_class')
        actual_class = data.get('actual_class')
        
        if not all([image_path, predicted_class, actual_class]):
            return jsonify({'error': 'Missing data'}), 400
            
        import csv
        from datetime import datetime
        
        log_file = 'feedback_log.csv'
        file_exists = os.path.isfile(log_file)
        
        with open(log_file, 'a', newline='') as f:
            writer = csv.writer(f)
            if not file_exists:
                writer.writerow(['Timestamp', 'Image Path', 'Predicted Class', 'Actual Class'])
            
            writer.writerow([datetime.now().strftime('%Y-%m-%d %H:%M:%S'), image_path, predicted_class, actual_class])
            
        return jsonify({'success': True})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    load_model()
    app.run(debug=True, host='0.0.0.0', port=5000)