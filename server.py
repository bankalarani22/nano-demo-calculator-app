from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/calculator/greeting", methods=['GET'])
def greeting():
    return "Welcome to the calculator API!"

@app.route("/calculator/add", methods=['POST'])
def add():
    data = request.json  # Assuming you're sending JSON data with 'num1' and 'num2' for addition
    if 'num1' in data and 'num2' in data:
        num1 = data['num1']
        num2 = data['num2']
        result = num1 + num2
        return jsonify({'result': result})
    else:
        return jsonify({'error': 'Invalid input'}), 400

@app.route("/calculator/subtract", methods=['POST'])
def subtract():
    data = request.json  # Assuming you're sending JSON data with 'num1' and 'num2' for subtraction
    if 'num1' in data and 'num2' in data:
        num1 = data['num1']
        num2 = data['num2']
        result = num1 - num2
        return jsonify({'result': result})
    else:
        return jsonify({'error': 'Invalid input'}), 400

if _name_ == '__main__':
    app.run(port=8080, host='0.0.0.0')

