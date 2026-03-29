🐾 FurAffecta – Pet Emotion Classification System

📌 Overview

FurAffecta is a Machine Learning–based system that analyzes pet images and predicts their emotional state.
The system uses image processing + classical machine learning models to classify pet emotions into:
😠 Angry
😊 Happy
😨 Scared
😢 Sad
It is designed to be lightweight, fast, and efficient, without requiring high-end hardware.

🎯 Objectives

->Develop an image-based pet emotion classification system<br>
->Implement ML models: Decision Tree, KNN, Random Forest, Logistic Regression<br>
->Classify pet emotions into predefined categories<br>
->Evaluate performance using standard metrics<br>

🛠️ Technologies Used

->Python – Core programming<br>
->OpenCV – Image preprocessing<br>
->HOG (Histogram of Oriented Gradients) – Feature extraction<br>
->Scikit-learn – Model training & evaluation<br>
->NumPy – Data processing<br>
->Matplotlib & Seaborn – Visualization<br>
->HTML & CSS – User interface<br>

⚙️ System Workflow

->Upload pet image<br>
->Preprocess image (resize, grayscale, noise removal)<br>
->Extract features using HOG<br>
->Pass features to trained ML model<br>
->Predict pet emotion<br>

📊 Model Performance
Model	Test Accuracy<br>
->Random Forest	92.23% <br>
->Logistic Regression	90.77%<br>
->Decision Tree	89.05%<br>
->KNN	49.59%<br>
👉 Best Performing Model: Random Forest<br>

📦 Project Structure

FurAffecta/
│── model/
│   └── pet_emotion.h5
│── static/
│── templates/
│── app.py
│── requirements.txt
│── README.md
│── LICENSE

⚙️ Setup Instructions

1. Clone the repository
git clone https://github.com/Sharanya-Aithal-KS/FurAffecta.git
cd FurAffecta

3. Install Git LFS ⚠️
This project uses Git LFS to handle large model files.
git lfs install
4. Create virtual environment
python -m venv venv

5. Activate environment
Windows:
venv\Scripts\activate
Mac/Linux:
source venv/bin/activate

6. Install dependencies
pip install -r requirements.txt

7. Run the project
python app.py

💡 Features

✔ Automatic pet emotion detection<br>
✔ Lightweight ML model<br>
✔ Fast prediction<br>
✔ Simple UI<br>
✔ Works on standard systems<br>

✅ Advantages

->Reduces manual interpretation errors<br>
->Fast and efficient<br>
->Low computational requirements<br>
->Easy to use<br>

⚠️ Limitations

->Depends on dataset quality<br>
->Limited feature representation (HOG)<br>
->Not suitable for subtle emotions<br>
->No real-time video support<br>

🚀 Future Enhancements

->Deep learning (CNN) integration<br>
->Real-time emotion detection<br>
->Mobile/web deployment<br>
->Larger dataset training<br>

📈 Results

->Achieved up to 92% accuracy<br>
->Stable and reliable predictions<br>
->Efficient on low-resource systems<br>

👩‍💻 Author
Sharanya Aithal KS

📜 License
This project is licensed under the MIT License.

⭐ Final Note
This project demonstrates how classical machine learning techniques can effectively solve real-world image classification problems with high accuracy and efficiency.

## 📸 Screenshots

### Homepage
![Homepage](screenshots/homepage.png)

### Prediction Results
![Prediction](screenshots/scared1.png)
![Prediction](screenshots/scared2.png)
![Prediction](screenshots/sad1.png)
![Prediction](screenshots/sad2.png)
![Prediction](screenshots/angry1.png)
![Prediction](screenshots/angry2.png)
![Prediction](screenshots/happy1.png)
![Prediction](screenshots/happy2.png)
