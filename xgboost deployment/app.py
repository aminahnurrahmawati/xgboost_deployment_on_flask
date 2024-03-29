import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
import json
from sklearn.preprocessing import StandardScaler
from cek import klasifikasi

sc = StandardScaler()

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    data = request.get_json(force=True)
    prediction = model.predict(sc.fit_transform([[np.array(list(data.values()))][0]]))
    print(prediction[0])

    output = klasifikasi(int(prediction[0]))

    return render_template('index.html', prediction_text='Employee Salary should be $ {}'.format(output))

@app.route('/predict_api',methods=['POST']) #
def predict_api():
    '''
    For direct API calls trought request
    '''
    data = request.get_json(force=True)
    prediction = model.predict(sc.fit_transform([[np.array(list(data.values()))][0]]))
    print(prediction[0])

    output = {'hasil prediksi': klasifikasi(int(prediction[0]))}
    return jsonify(output)

if __name__ == "__main__":
    app.run(debug=True)

"""{
    "Area":28395,
    "Perimeter":638.018,
    "MajorAxisLength":212.826130,
    "MinorAxisLength":175.931143,
    "AspectRation":1.197191
    } #example of body"""