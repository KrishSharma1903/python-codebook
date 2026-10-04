#Intergrating HTML files in the framework
from flask import Flask, render_template #(helps to redirect to another HTML page)

##WSGI application
app=Flask(__name__)
@app.route("/")
def welcome():
    return "<html><h1>Welcome to flask!</h1></htlml>"

@app.route("/index")
def index():
    return render_template('index.html')#will look for index.html inside a folder named template which we need to create by ourself

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ =="__main__":
    app.run(debug=True) 
