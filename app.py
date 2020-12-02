import numpy as np
from flask import Flask,request,jsonify,render_template
import pickle

app=Flask(__name__)
model=pickle.load(open('model.pkl','rb'))

@app.route('/')

def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])

def predict():
    '''
    for rendering result on HTML GUI
    '''
    # int_feature=[int(x) for x in request.form.values()]
    # final_fetaures=[np.array(int_feature)]
    #use above code or below code

    exp=request.form.get('experience')
    test_score=request.form.get('test_score')
    interview_score=request.form.get('interview_score')

    #convert all the features into numeric
    int_feature=[int(exp) ,int(test_score) ,int(interview_score)]
    final_fetaures=[np.array(int_feature)]
    prediction=model.predict(final_fetaures)
    output =round(prediction[0],2)
    return render_template('index.html',predtion_text='Employee Salary should be ${}'.format(output))

if __name__ == "__main__":
    app.run(debug=True)