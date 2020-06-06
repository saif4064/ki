#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from flask import Flask,request,jsonify,render_template,url_for
from werkzeug.utils import secure_filename
import os
import pickle
from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array





app=Flask(__name__)
location=r"static/"
app.config['Upload_Folder']=location





@app.route('/')
def home():
    return render_template('index.html')
@app.route('/predict',methods=['GET','Post'])
def predict():
    return render_template('index.html')
if __name__=="__main__":
    app.run(debug=True, use_reloader=False)


# In[ ]:




