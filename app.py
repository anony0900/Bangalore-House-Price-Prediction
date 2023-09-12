from flask import Flask, request, jsonify, render_template
import util

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('app.html')

@app.route('/get_location_names', methods=['GET'])
def get_location_names():
    response = jsonify({
        'locations': util.get_location_names()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

@app.route('/prediction', methods=['GET', 'POST'])
def predict_home_price():
    if request.method == 'POST':
        total_sqft = float(request.form['total_sqft'])
        location = request.form['location']
        bhk = float(request.form['uiBHK'])
        bath = float(request.form['uiBathrooms'])

        response = util.get_estimated_price(location,total_sqft,bhk,bath)
        print(response)
        return render_template('app.html', prediction=response, million = 'million')

if __name__ == "__main__":
    print("Starting Python Flask Server For Home Price Prediction...")
    util.load_saved_artifacts()
    app.run()