from flask import Flask, jsonify, request
from datetime import datetime
import os

app = Flask(__name__)
app.config['VERSION'] = os.getenv('APP_VERSION', '1.0.0')


@app.route('/')
def home():
    return jsonify({
        'message': 'Welcome to Python CI/CD API',
        'version': app.config['VERSION'],
        'timestamp': datetime.now().isoformat()
    })


@app.route('/health')
def health():
    return jsonify({'status': 'healthy'}), 200


@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.get_json()
    if not data or 'a' not in data or 'b' not in data:
        return jsonify({'error': 'Missing parameters a or b'}), 400

    operation = data.get('operation', 'add')
    a = data['a']
    b = data['b']

    if operation == 'add':
        result = a + b
    elif operation == 'subtract':
        result = a - b
    elif operation == 'multiply':
        result = a * b
    elif operation == 'divide':
        if b == 0:
            return jsonify({'error': 'Division by zero'}), 400
        result = a / b
    else:
        return jsonify({'error': 'Invalid operation'}), 400

    return jsonify({'result': result, 'operation': operation})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)