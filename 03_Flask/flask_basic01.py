from flask import Flask 

##WSGI application
app=Flask(__name__)#It creates an instance of the flask class which will be your WSGI(Web Server Gateway Interface) application
@app.route("/")
def welcome():
    return "Welcome to flask!"

@app.route("/index")
def index():
    return "Welcome to the index page"


if __name__ =="__main__": #This is the entry point of a py file and this will be checked first whenever we run the code file
    app.run(debug=True) #this is used to make changes while developing and restarts the server 

