from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hey dumb dumb"

if __name__ == '__main__':
    app.run(debug=True)