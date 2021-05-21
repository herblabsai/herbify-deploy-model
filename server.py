# Import the modules
from flask import Flask, request, jsonify, make_response
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.models import load_model
import cv2
import numpy as np
import uuid
from flask_cors import CORS, cross_origin

# Model label
names = ["Adas", "Akar Alang Alang", "Bawang Putih", "Daun Katuk", "Daun Salam", "Jahe", "Kapulaga", "Kumis Kucing", "Kunyit", "Lidah Buaya", "Mengkudu", "Meniran", "Miana", "Pare", "Pegagan", "Rosela", "Seledri", "Serai", "Temu Kunci", "Valerian"]

# Process image and predict label
def predict_image(IMG_PATH):
    # Load the model
    model = load_model("model_xception_herbify.h5")
    
    # Preprocess the image
    image = cv2.imread(IMG_PATH)
    image = cv2.resize(image, (199, 199))
    image = image.astype("float") / 255.0
    image = img_to_array(image)
    image = np.expand_dims(image, axis=0)

    # Predict the image
    res = model.predict(image)
    label = np.argmax(res)

    # Print out the label
    print("Label", label)
    labelName = names[label]
    print("Label name:", labelName)
    return labelName


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
    # Get the posted data
    data = request.get_json(force=True)
    uid = data['uid']

    # Get image
    img = request.files["img"]

    # Save the image with unique name
    img_file = str(uuid.uuid1()) + ".jpg"
    img.save(img_file)

    # Predict the image
    predict_result = predict_image(img_file)

    response = {
        'uid': uid,
        'predictResult': predict_result
    }

    # Return response
    return make_response(jsonify(response), 200)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
