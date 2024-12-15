from flask import Flask, render_template,request
import modelll
import os
import modelll 

import FeatureExtraction
import numpy as np
PEOPLE_FOLDER = os.path.join('static', 'img')


app = Flask(__name__,static_url_path='/static')
app.config['UPLOAD_FOLDER'] = PEOPLE_FOLDER



def submit():
    # Perform any processing or computations here
    # Simulate a delay for demonstration purposes
    
    # time.sleep(2)
    full_filename = os.path.join(app.config['UPLOAD_FOLDER'], '33.png')
    company_logo = os.path.join(app.config['UPLOAD_FOLDER'], '33.png')
    reloader_img = os.path.join(app.config['UPLOAD_FOLDER'], 'loaderr.gif')
    # Redirect back to home page after processing
    return render_template("home.html", user_image = full_filename,company_logo=company_logo,csshai= "static/style.css",loading_img = reloader_img)

# def index():
#  return '<h1>Hello World!</h1>'
@app.route('/',methods=['GET'])
def home():
    full_filename = os.path.join(app.config['UPLOAD_FOLDER'], '33.png')
    company_logo = os.path.join(app.config['UPLOAD_FOLDER'], '33.png')
    return render_template("home.html", user_image = full_filename,company_logo=company_logo,csshai= "static/style.css")
    #return render_template('home.html')

@app.route('/about')
def hhome():
    return render_template('about.html')

@app.route('/faq')
def faq():
    return render_template('faq.html')

@app.route('/about-more')
def aboutt():
    return render_template('about-more.html')

# @app.route('/user/<name>')
# def user(name):
#  return '<h1>Hello, %s!</h1>' % name

@app.route('/', methods=['POST'])
def predict():

    # l= [1,1,0,1,1,1,-1,-1,-1,-1,1,1,-1,1,0,-1,-1,-1,-1,0,1,1,1,1,1,-1,1,-1,1,0,-1]
    value = []
    # for x in request.form['urlname'].split(','):
    #     value.append(int(x)) 
    # ob = modelll.mode()
    # o = ob.just(value)
    # print(o[0])
    # res = ''
    # if(o[0] != 1):
    #    res = 'This url is safe to view' 
    # else:
    #     res = 'this URL  can be phishing url'
    full_filename = os.path.join(app.config['UPLOAD_FOLDER'], '33.png')
    company_logo = os.path.join(app.config['UPLOAD_FOLDER'], '33.png')
    # reloader_img = os.path.join(app.config['UPLOAD_FOLDER'], 'loaderr.gif')
   
    # # l= [1,1,0,1,1,1,-1,-1,-1,-1,1,1,-1,1,0,-1,-1,-1,-1,0,1,1,1,1,1,-1,1,-1,1,0,-1]
    # submit()
    # print(request.form['urlname'])
    
    res = ""
    obj = FeatureExtraction.FeatureExtraction(request.form['urlname'])
    value = obj.getFeaturesList()
    x = np.array(value).reshape(1,30) 

    objectofmodel = modelll.mode()
    o = objectofmodel.just(x)
    if o[0] == 1:
        res = "This URL seem to be safe to view."
    else:
        res = "Caution! Suspicious website detected"
    
    return render_template("home.html", user_image = full_filename,company_logo=company_logo,csshai= "static/style.css",result = res)
    # return render_template('home.html',result = res )
 
 
if __name__ == '__main__':
 app.run(debug=True)







