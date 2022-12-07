from flask import Flask, jsonify, render_template, redirect, request, url_for
import config1
from utils import MedicalInsurence
app = Flask(__name__)

@app.route('/predict',methods = ['GET', "POST"])
def prediction():
    if request.method == 'POST':
        data = request.form
        
        print('data :',data)

        med_ins = MedicalInsurence(data)
        price = med_ins.get_predicted_price()
        print("::::::::::",price)
        return jsonify({"Price :":price})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=config1.PORT_NUMBER)

