from flask import Flask,request, url_for, redirect, render_template, jsonify
from pycaret.regression import *
import pandas as pd
import pickle
import numpy as np

app = Flask(__name__)

model = load_model('Finallrmodel20Jan2021')

cols = ['age', 'sex', 'color_of_skin','respiratory_rate','use_of_accessory_muscles','lung_auscultation','brain_function','heart_rate']

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/predict',methods=['POST'])
def predict():
    int_features = [x for x in request.form.values()]
    print(int_features)
    final = np.array(int_features)
    data_unseen = pd.DataFrame([final], columns = cols)
    prediction = predict_model(model, data=data_unseen, round = 0)
    print(prediction)
    prediction = prediction.Label[0]
    if prediction==0:
        prediction = 'Mild'
    elif prediction == 1:
        prediction = 'Moderate'
    else:
        prediction='Severe'

    return render_template('home.html',pred='Curent Asthma is {}'.format(prediction))
    



if __name__ == '__main__':
    app.run(debug=True)
