from flask import Flask
from fetch import *
app = Flask(__name__)

def fetch_data(pair):



@app.route('/')
def hello_name():
    return 'Hello !' 

@app.route('/fetch/<name>')
def download(name):
    fetch(name)
    return 'On it!'



if __name__ == '__main__':
    app.run()


