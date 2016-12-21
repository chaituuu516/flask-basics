from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World! this is chaituu"

@app.route("/hello")
def hell():
    return "Hello user! this is chaituu"

if __name__ == "__main__":
    app.run()
