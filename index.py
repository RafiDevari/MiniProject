from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/hello')
def index():
    return "Hello, World!"

if __name__ == '__main__':
    app.run(debug=True)