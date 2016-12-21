from flask import Flask

app = Flask(__name__)

@app.route('/')

def index():
    return 'this is chaitu'

@app.route('/<username>')
def profile(username):
    return '<h1>Hi %s.. How are u</h1>' %username
    return '<h3>this is sample</h3>'

if __name__ == "__main__":
    app.run() 
