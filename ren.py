from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('bdemo.html')  # Assuming bdemo.html exists in templates folder

# Creating endpoints
@app.route('/about_me')
def about():
    return "Hello my name is Tanushka"

@app.route('/contact')
def cont():
    return "You can contact me via email abc100@gmail.com"

if __name__ == "__main__":
    app.run(debug=True, port=7000)
