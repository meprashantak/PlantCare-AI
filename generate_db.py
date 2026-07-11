import json

classes = [
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

disease_info = {}

for cls in classes:
    plant = cls.split('___')[0].replace('_', ' ')
    disease = cls.split('___')[1].replace('_', ' ')
    
    if 'healthy' in disease.lower():
        disease_info[cls] = {
            "description": f"The {plant} plant appears to be healthy and free of major diseases.",
            "treatment": "No treatment necessary. Continue with regular watering and fertilizing schedules.",
            "prevention": "Maintain good agricultural practices, ensure proper spacing, and monitor regularly for any signs of pests or disease."
        }
    else:
        disease_info[cls] = {
            "description": f"The {plant} plant is showing symptoms of {disease}. This is a common disease affecting {plant} crops that can reduce yield if left untreated.",
            "treatment": f"1. Remove and destroy infected plant parts immediately.\n2. Apply appropriate fungicides or bactericides labeled for {disease} on {plant}.\n3. Ensure good air circulation around the plants.",
            "prevention": f"1. Practice crop rotation.\n2. Use disease-resistant varieties if available.\n3. Avoid overhead watering to keep foliage dry.\n4. Sanitize garden tools regularly."
        }

with open('disease_info.json', 'w') as f:
    json.dump(disease_info, f, indent=4)

print("Generated disease_info.json successfully!")
