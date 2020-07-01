from flask import Flask, render_template, request
import jsonify
import requests
import pickle
import numpy as np
import sklearn
from sklearn.preprocessing import StandardScaler
import datetime

app = Flask(__name__)

model = pickle.load(open('car_price_predict.pkl', 'rb'))
model = pickle.load(open('car_price_predict1.pkl', 'rb'))


@app.route('/')
def hello_world():
    return render_template('index.html')


standard_to = StandardScaler()


@app.route('/predict', methods=['post'])
def predict():
    if request.method == 'POST':
        year = int(request.form['year'])
        no = datetime.datetime.now()
        no_of_year = no.year - year
        Actualprice = request.form['aprice']
        km = request.form['km']
        owner = request.form['owner']
        Fuel = request.form['Fuel']
        otype = request.form['otype']
        trans = request.form['trans']
        predict = model.predict([[no_of_year, Actualprice, km, owner, Fuel, otype, trans]])
        print(predict)
        if predict < 0:
            return render_template('index.html', output = "Sorry you cannot sell this car")
        else:
            return render_template('index.html', output="You Can Sell The Car at {} lakhs according to Cardekho".format(predict))


if __name__ == '__main__':
    app.run()
