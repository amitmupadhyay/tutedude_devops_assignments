from flask import Flask, jsonify
import json

app = Flask(__name__)

@app.route('/')
def index():
  strIndex = "<h1>Flask & MongoDB Assignment</h1><hr><h2>Jump to</h2><h3><a href='/api'>/api</a></h3>"
  return strIndex

@app.route('/api')
def get_data():

    # Read data from backend file
    with open('data.json', 'r') as file:
        data = json.load(file)

    # Return JSON response
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)