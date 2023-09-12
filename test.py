import util

def predict_home_price():
    # total_sqft = float(request.form['total_sqft'])
    # location = request.form['location']
    # bhk = float(request.form['uiBHK'])
    # bath = float(request.form['uiBathrooms'])

    total_sqft =  1500
    location = 'Ejipura'
    bhk = 3
    bath = 2

    response = util.get_estimated_price(location,total_sqft,bhk,bath)
    # response.headers.add('Access-Control-Allow-Origin', '*')
    print(response)


if __name__ == "__main__":
    util.load_saved_artifacts()
    predict_home_price()