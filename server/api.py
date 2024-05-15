from flask import Flask, request, jsonify
import base64
import io
from image_processing import adjust_brightness

app = Flask(__name__)


@app.route('/process-image', methods=['POST'])
def process_image():
    try:
        img_b64 = request.json['image']
        img = base64.b64decode(img_b64)
        enhanced_image = adjust_brightness(img, 1.3)
        buffered = io.BytesIO()
        # Save the processed image into new buffer, with format JPEG
        enhanced_image.save(buffered, format="JPEG")
        encoded_image = base64.b64encode(buffered.getvalue()).decode('utf-8')

        return jsonify({"image": encoded_image})
    except Exception as e:
        return jsonify({"image": None, "error": str(e)}), 400
