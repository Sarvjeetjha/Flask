from flask import Flask

'''
 It creates an instance of the Flask class, 
 which will be your WSGI (Web Server Gateway Interface) application.
'''
#wsgi(Web server getway interface) Application
app=Flask(__name__)
@app.route("/")
def welcom():
    return "This is best  Flask course .This should be an amzing course"


@app.route("/index")
def index():
    return "this is index page"
if __name__=="__main__":
    app.run(debug=True)
