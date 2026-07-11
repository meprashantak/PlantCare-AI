# 🌿 PlantCare AI – Plant Disease Detection Using Transfer Learning

## 📌 Overview

PlantCare AI is a Deep Learning-based web application that detects plant diseases from leaf images using Transfer Learning with MobileNetV2.

The application enables users to upload an image of a plant leaf and instantly predicts the disease along with its confidence score, disease description, treatment suggestions, and preventive measures.

This project was developed using Python, TensorFlow/Keras, Flask, HTML, CSS, and JavaScript.

---

## 🚀 Features

* 🌱 Plant disease detection from leaf images
* 🤖 MobileNetV2 Transfer Learning model
* 📊 Supports 38 plant disease classes
* 📈 Confidence score for predictions
* 💊 Disease treatment recommendations
* 🛡️ Disease prevention guidelines
* 🌐 Responsive Flask web application
* 📝 User feedback collection

---

## 🛠️ Tech Stack

### Programming Language

* Python

### Deep Learning

* TensorFlow
* Keras
* MobileNetV2

### Web Framework

* Flask

### Frontend

* HTML
* CSS
* JavaScript

### Libraries

* NumPy
* Pillow
* Werkzeug

---

## 📂 Project Structure

```
PlantCare-AI/
│
├── app.py
├── mobilenetv2_best.keras
├── disease_info.json
├── generate_db.py
├── plant Disease Detection.ipynb
├── requirements.txt
├── README.md
│
├── templates/
│   ├── home.html
│   ├── about.html
│   ├── upload.html
│   └── result.html
│
├── static/
│   ├── style.css
│   ├── theme.js
│   └── images/
│
└── uploads/
```

---

## 🧠 Model

* Model Architecture: MobileNetV2
* Technique: Transfer Learning
* Input Size: 224 × 224 RGB
* Output Classes: 38
* Framework: TensorFlow/Keras

---

## 📊 Dataset

The model was trained using the **New Plant Diseases Dataset**, which contains over **87,000** augmented images covering **38 plant disease categories**.

---

## ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/meprashantak/PlantCare-AI.git
```

Move into the project folder

```bash
cd PlantCare-AI
```

Create a virtual environment

```bash
python -m venv venv
```

Activate the virtual environment

Windows

```bash
venv\Scripts\activate
```

Linux / macOS

```bash
source venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
python app.py
```

Open your browser

```
http://127.0.0.1:5000
```

---

## 📷 How It Works

1. Upload a plant leaf image.
2. The image is resized to 224×224.
3. MobileNetV2 predicts the disease.
4. The application displays:

   * Predicted disease
   * Confidence score
   * Disease description
   * Treatment
   * Prevention tips

---

## 🎯 Future Improvements

* Mobile application
* Cloud deployment
* Real-time camera detection
* Multi-language support
* Additional crop disease support
* Higher model accuracy through expanded datasets

---

## 👨‍💻 Author

**Prashant K**

GitHub: https://github.com/meprashantak

LinkedIn: *(Add your LinkedIn profile here)*

---

## ⭐ If you found this project useful

Please consider giving this repository a **Star ⭐**.
