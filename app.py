from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import joblib, os

app = Flask(__name__, static_folder="static", template_folder="templates")
CORS(app)

# Paths to saved artifacts
MODEL_PATH      = "fraud_pipeline.joblib"

# Ensure the model exists
if not os.path.exists(MODEL_PATH):
    raise FileNotFoundError(f"Model file not found: {MODEL_PATH}")

# Load the full pipeline
pipeline = joblib.load(MODEL_PATH)


@app.route('/', methods=['GET'])
def home():
    # Serve templates/index.html
    return render_template('index.html')


@app.route('/detect', methods=['POST'])
def detect():
    data = request.get_json(force=True) or {}
    message = data.get('message', '').strip()

    if not message:
        return jsonify(error="No message provided"), 400

    try:
        pred = pipeline.predict([message])[0]
        label = "Fraudulent" if pred == 1 else "Non-Fraudulent"
        return jsonify(result=label)
    except Exception as e:
        return jsonify(error=str(e)), 500


if __name__ == '__main__':
    # In development: debug=True; in prod drop it.
    app.run(port=5001, debug=True)
