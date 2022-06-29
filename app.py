from flask import Flask

app = Flask(__name__)

@app.route('/')
def new():
    return 'Hello World Changed'

if __name__ == '__main__':
    app.run()