from flask import Flask, render_template, jsonify
from flask import Response

app = Flask(__name__)
CORS(app)



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)