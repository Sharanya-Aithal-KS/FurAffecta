from flask import Flask, render_template, request
import numpy as np
from PIL import Image
from tensorflow.keras.models import load_model
import os

app = Flask(__name__)

# Load model once when app starts
model = load_model("model/pet_emotion.h5")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/pet-emotion-predict", methods=["POST"])
def pet_emotion_predictPage():
    pred = None

    try:
        if "image" not in request.files:
            return render_template("index.html", message="No file selected.")

        file = request.files["image"]

        if file.filename == "":
            return render_template("index.html", message="Please upload an image.")

        # Convert image to RGB (important!)
        img = Image.open(file).convert("RGB")
        img = img.resize((224, 224))

        x = np.asarray(img)
        x = np.expand_dims(x, axis=0)
        x = x / 255.0

        prediction = model.predict(x)
        pred = int(np.argmax(prediction, axis=1)[0])

    except Exception as e:
        print("Error:", e)
        return render_template("index.html", message="Error during recognition. Try again.")

    return render_template("predict.html", pred=pred)

if __name__ == "__main__":
    app.run(debug=True)