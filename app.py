from flask import Flask, request, jsonify
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
# ... [import other necessary libraries] ...

app = Flask(__name__)

# Here you'll load your trained model (consider using joblib to save and load the model)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json(force=True)
    prediction = model.predict([data['message']])
    return jsonify(prediction=prediction[0])

if __name__ == '__main__':
    app.run(debug=True)