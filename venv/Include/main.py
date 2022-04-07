from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/products")
def hello_world():
    return "This is product page"

if __name__== "__main__" :
    app.run(debug=True) #run in debug mode so that we can see the error
    