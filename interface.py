from flask import Flask, request, jsonify
from utils import MedicalInsurence
app = Flask(__name__)

@app.route('/')
def home():
    
    return jsonify({"Result":"Successful"})

@app.route('/medical_insurence/predict_charges')
def predict_charges():
    data = request.form
    print("Data :",data)
    age      = data['age']
    gender   = data['gender']
    bmi      = data['bmi']
    children = data['children']
    smoker   = data['smoker']
    region   = data['region']

    pred_price = get_predicted_price(age,gender,bmi,children,smoker,region)
    
    return jsonify({"Result":f"Predicted Medical Charges == {pred_price}"})
 
if __name__ == "__main__":
    app.run(host = "0.0.0.0",config.PORT_NUMBER)
    
