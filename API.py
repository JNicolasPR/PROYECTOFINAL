from flask import Flask, request, jsonify
import joblib
import numpy as np

app = Flask(__name__)
model = joblib.load('modelo_entrenado2.pkl')


@app.route('/predict/API/nn', methods=['POST'])
def predict():
    if request.is_json:
        data = request.get_json()

        if 'feature' in data:
            features = data['feature']
            features_array = np.array(list(features.values())).reshape(1, -1)
            prediction = model.predict(features_array)

            return jsonify({'prediction': prediction[0]})

        else:
            return jsonify({"error": "El JSON no tiene la clave 'feature'"}), 400

    else:
        return jsonify({"error": "Contenido no es JSON"}), 400


if __name__ == '__main__':
    app.run(debug=False, host = 'http://container_2', port=8000)
