# Import the modules
from flask import Flask, request, jsonify, make_response
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.xception import preprocess_input
from tensorflow.keras.models import load_model
import numpy as np
import uuid
import subprocess
from flask_cors import CORS, cross_origin

# Model label
labels = ["Adas", "Akar Alang Alang", "Bawang Putih", "Daun Katuk", "Daun Salam", "Jahe", "Kapulaga", "Kumis Kucing", "Kunyit",
          "Lidah Buaya", "Mengkudu", "Meniran", "Miana", "Pare", "Pegagan", "Rosela", "Seledri", "Serai", "Temu Kunci", "Valerian"]

# Process image and predict label


def predict_image(IMG_PATH):
    # Load the model
    model = load_model("model_xception_herbify.h5")

    # Preprocess the image
    img = image.load_img(IMG_PATH, target_size=(299, 299))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    x = preprocess_input(x)

    # Predict the image
    images = np.vstack([x])
    proba = model.predict(images)[0]

    # Cloud Storage URL for storing placeholder images
    URL = "https://storage.googleapis.com/herbify/herb-placeholder/"

    # Create dict to save the results
    arr_data = []
    for (label, p) in zip(labels, proba):
        # Append the result to arr_data
        result = dict(
            {"name": label, "confident": float("{:.2f}".format(p * 100)), "imageUrl": URL + label + ".jpg"})
        arr_data.append(result)

    return {"data": arr_data}


# Initializing flask application
app = Flask(__name__)
cors = CORS(app)


@app.route("/")
def main():
    return """
        Application is ready to predict
    """

# Endpoint for upload the image


@app.route("/predict", methods=["POST"])
def process_req():
    # Get image
    img = request.files["img"]

    # Save the image with unique name
    img_file = str(uuid.uuid1()) + ".jpg"
    img.save(img_file)

    # Predict the image
    predict_result = predict_image(img_file)

    # Move image to cloud storage
    subprocess.run(["gsutil", "mv", img_file, "gs://herbify/upload-images/"])

    # Add img_file to response
    image_name = {"imageUploaded": img_file}

    # Return response
    return make_response(jsonify({**image_name, **predict_result}), 200)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
