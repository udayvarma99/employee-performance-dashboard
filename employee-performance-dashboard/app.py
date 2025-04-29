from flask import Flask, render_template, jsonify
import json

app = Flask(__name__)

# Load employee data
def load_data():
    with open('data.json', 'r') as f:
        return json.load(f)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/data')
def data():
    return jsonify(load_data())

if __name__ == '__main__':
    app.run(debug=True)
