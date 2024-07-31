from flask import Flask,render_template,request,url_for,redirect

'''
 It creates an instance of the Flask class, 
 which will be your WSGI (Web Server Gateway Interface) application.
'''
#wsgi(Web server getway interface) Application
app=Flask(__name__)
@app.route("/")
def welcom():
    return "<html><h1>This is my flask webPage</h1></html>"

@app.route("/index",methods=['GET'])#by default methods is GET
def index():
    return render_template("index.html")
@app.route("/about")
def about():
    return render_template("about.html")
@app.route("/form",methods=['GET','POST'])
def form():
    if request.method=='POST':
        name=request.form['name']
        return f'Hello {name} !'
    return render_template('form2.html')
# @app.route("/submit",methods=['GET','POST'])
# def submit():
#     if request.method=='POST':
#         name=request.form['name']
#         return f'Hello {name} !'

#     return render_template('form2.html')
##variable Rule

@app.route('/success/<int:score>')
def success(score):
    return f"Hey you got mark : "+str(score)
@app.route('/success2/<int:score>')
def success2(score):
    res=""
    if score >50:
        res="PASSED"
    else:
        res="FAILED"
    return render_template('result.html',result=res)
@app.route('/successres/<int:score>')
def successres(score):
    d=dict()
    res=""
    if score>50:
        d['score']=score
        d['result']="Pass"
    else:
        d['score']=score
        d['result']="Fail"
    return render_template('successres.html',result=d)
#if condition
@app.route('/submit',methods=['GET','POST'])
def submit():
    if request.method=='POST':
        science=float(request.form['science'])
        maths=float(request.form['maths'])
        c=float(request.form['c'])
        datascience=float(request.form['datascience'])
        avg=(science+maths+c+datascience)/4
        return redirect(url_for('successres',score=avg))
    else:
        return render_template('getreasult.html')
if __name__=="__main__":
    app.run(debug=True)
