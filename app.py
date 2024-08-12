from flask import Flask,render_template,redirect,url_for,request
import pickle
import os
import pandas as pd
import numpy as np

path=os.getcwd()
model_folder= 'model'
#pkl file name
model_pickle='model.pkl'
##join path
model_path=os.path.join(path,model_folder,model_pickle)
#load model
model = pickle.load(open(model_path,'rb'))

app=Flask(__name__)

@app.route('/')
def page():
    return render_template('index.html')

@app.route('/predict', methods=["POST"])
def final():
    if request.method == 'POST':
        ram = int(request.form['ram'])
        px_height = int(request.form['px_height'])
        px_width = int(request.form['px_width'])
        power = int(request.form['power'])
        
        data = np.array([[ram,px_height,px_width,power]])
        my_prediction = model.predict(data)
        
        return render_template('index1.html', prediction=my_prediction)


if __name__=='__main__':
    app.run(debug=True)

