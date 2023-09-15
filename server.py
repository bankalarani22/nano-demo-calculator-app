from flask import Flask

app = Flask(__name__)

@app.route("/calculator/greeting", methods=['GET'])
def greeting():
    return "Welcome to the calculator app!"

@app.route("/calculator/add", methods=['POST'])
def add():
    return "This is the addition route."

@app.route("/calculator/subtract", methods=['POST'])
def subtract():
    return "This is the subtraction route."

if __name__ == '__main__':
    app.run(port=8080, host='0.0.0.0')

