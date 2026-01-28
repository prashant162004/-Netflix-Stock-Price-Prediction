import numpy as np
import pickle
from flask import Flask, request, render_template, jsonify

# Load model
model = None
try:
    model = pickle.load(open('model.pkl', 'rb'))
except Exception as e:
    print(f'Warning: Could not load model: {e}')

app = Flask(__name__, template_folder='templates')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.form
        features = np.array([[
            float(data.get('Open', 0)),
            float(data.get('High', 0)),
            float(data.get('Low', 0)),
            float(data.get('Adj_Close', 0)),
            float(data.get('Volume', 0)),
            float(data.get('year', 0)),
            float(data.get('month', 0)),
            float(data.get('day', 0))
        ]])
        
        if model is None:
            return render_template('index.html', output='Model not loaded')
        
        prediction = model.predict(features)[0]
        return render_template('index.html', output=f'${prediction:.2f}')
    except Exception as e:
        return render_template('index.html', output=f'Error: {str(e)}')

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)



    