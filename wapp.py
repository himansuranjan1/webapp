import pickle
from flask import Flask, render_template, request
import numpy as np
app = Flask(__name__)
model=pickle.load(open('model.pkl','rb'))


@app.route('/')
def idx():
    return render_template('idx.html')
@app.route('/predict',methods=['GET','POST'])
def predict():
   
   # print(model.predict([[2, 9, 6]]))
  # ans=model.predict(request.form.get())
   int_features = [int(x) for x in request.form.values()]
   final_features = [np.array(int_features)]
   prediction = model.predict(final_features)

   output = round(prediction[0], 2)

   return render_template('idx.html', prediction_text='Employee Salary should be $ {}'.format(output))
  # return render_template('idx.html')
if __name__=="__main__":
    app.run(debug=True)