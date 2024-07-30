from flask import Flask,render_template

'''
 It creates an instance of the Flask class, 
 which will be your WSGI (Web Server Gateway Interface) application.
'''
#wsgi(Web server getway interface) Application
app=Flask(__name__)
@app.route("/")
def welcom():
    return "<html><h1>This is my flask webPage</h1></html>"

@app.route("/index")
def index():
    return render_template("index.html")
@app.route("/about")
def about():
    return render_template("about.html")
if __name__=="__main__":
    app.run(debug=True)
