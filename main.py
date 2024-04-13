from flask import Flask, render_template, jsonify

app = Flask(__name__)
# CORS(app)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/api/login/', methods =['POST'])
def home3():
    response = jsonify({'token':1234})
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.status=200
    return response

@app.route('/api/downloads/', methods =['POST'])
def home2():
    response = jsonify({'series':5715, 'number':617472})
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.status=200
    return  response

if __name__ == '__main__':
    app.run(debug=True)