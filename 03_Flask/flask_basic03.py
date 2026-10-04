from flask import Flask, render_template, request

# Create the Flask application
app = Flask(__name__)


# Route for the home page
@app.route("/")
def welcome():
    return "<html><h1>Welcome to Flask!</h1></html>"


# Route for the index page
# GET is used because we are only displaying the page
@app.route("/index", methods=["GET"])
def index():
    return render_template("index.html")


# Route for the about page
@app.route("/about")
def about():
    return render_template("about.html")


# Route for displaying and submitting the form
# GET  -> display the form
# POST -> receive the data submitted by the user
@app.route("/form", methods=["GET", "POST"])
def form():

    # Check whether the user submitted the form
    if request.method == "POST":
        # The 'name' here must match name="name" in HTML
        name = request.form["name"]
        return f"Hello {name}"

    
    return render_template("form.html")


# Run the Flask development server
if __name__ == "__main__":
    app.run(debug=True)