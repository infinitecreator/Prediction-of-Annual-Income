import numpy as np
from flask import Flask, request, jsonify
import pickle # to load the trained model

# creating the instance of the app
app = Flask(__name__)
# loading the trained model
model = pickle.load(open('model.pkl','rb'))

@app.route('/api',methods = ['POST'])
def predict():
    # get the data from the POST request

    data = request.get_json(force= True)

    #predict on the POST requested data by first converting to the 2d arrays

    prediction = model.predict([[np.array(data['exp'])]])


    output = prediction[0]

    # return the output by converting the data into the json file first
    return jsonify(output)

if __name__  == '__main__':
    app.run(debug = True, port  = 5000)
