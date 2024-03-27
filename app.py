from flask import Flask

app = Flask(__name__)
@app.route("/")
def hello_world():
    return"<p>Hello World</p>"
#creating end points
@app.route('/about_me')
def about():
    return "Hello my name is Tanushka"
@app.route('/contact')
def cont():
    return "You can contact me via email abc100@gmail.com"
if __name__ == "__main__":
    app.run(debug=True)