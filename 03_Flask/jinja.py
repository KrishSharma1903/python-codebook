from flask import Flask, render_template, request, redirect, url_for

# Create Flask app
app = Flask(__name__)


# Home page
@app.route("/")
def welcome():
    return "<html><H1>Welcome to the flask course</H1></html>"


# Render index.html
@app.route("/index", methods=['GET'])
def index():
    return render_template('index.html')


# Render about.html
@app.route('/about')
def about():
    return render_template('about.html')


# Dynamic URL: /success/75
# <int:score> gets score from the URL
@app.route('/success/<int:score>')
def success(score):
    res = ""

    if score >= 50:
        res = "PASSED"
    else:
        res = "FAILED"

    # Send result to HTML
    return render_template('result.html', results=res)


# Dynamic URL + dictionary
@app.route('/successres/<int:score>')
def successres(score):

    if score >= 50:
        res = "PASSED"
    else:
        res = "FAILED"

    # Store score and result together
    exp = {'score': score, 'res': res}

    return render_template('result1.html', results=exp)


# Send score to HTML
# Jinja can perform the if condition
@app.route('/sucessif/<int:score>')
def successif(score):
    return render_template('result.html', results=score)


# Another dynamic URL example
@app.route('/fail/<int:score>')
def fail(score):
    return render_template('result.html', results=score)


# Handle form submission
@app.route('/submit', methods=['POST', 'GET'])
def submit():

    total_score = 0

    if request.method == 'POST':

        # Get values submitted from HTML form
        science = float(request.form['science'])
        maths = float(request.form['maths'])
        c = float(request.form['c'])
        data_science = float(request.form['datascience'])

        # Calculate average
        total_score = (science + maths + c + data_science) / 4

    else:
        # GET → show the form
        return render_template('getresult.html')

    # Redirect to successres with calculated score
    return redirect(url_for('successres', score=total_score))


# Start Flask server
if __name__ == "__main__":
    app.run(debug=True)