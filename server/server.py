from flask import Flask, render_template, request, jsonify
import util

app = Flask(__name__)

@app.route('/')
def home():
    # Fetch locations for the dropdown
    try:
        locations = util.get_location_names()
    except Exception as e:
        locations = []
        print(f"Error fetching locations: {e}")
    
    return render_template('index.html', 
                           locations=locations, 
                           default_sqft=1000,
                           default_bhk=2,
                           default_bath=2)

@app.route('/predict_home_price', methods=['POST'])
def predict_home_price():
    try:
        total_sqft = float(request.form['total_sqft'])
        location = request.form['location']
        bhk = int(request.form['bhk'])
        bath = int(request.form['bath'])

        estimated_price = util.get_estimated_price(location, total_sqft, bhk, bath)
        
        return render_template('index.html', 
                               locations=util.get_location_names(),
                               total_sqft=total_sqft,
                               bhk=bhk,
                               bath=bath,
                               location=location,
                               estimated_price=estimated_price,
                               default_sqft=total_sqft,
                               default_bhk=bhk,
                               default_bath=bath)
    except Exception as e:
        return render_template('index.html', 
                               locations=util.get_location_names(),
                               error=str(e),
                               default_sqft=1000,
                               default_bhk=2,
                               default_bath=2)

@app.route('/get_location_names', methods=['GET'])
def get_location_names():
    return jsonify({
        'locations': util.get_location_names()
    })

if __name__ == "__main__":
    print("Starting Python Flask Server For Home Price Prediction...")
    util.load_saved_artifacts()
    app.run(debug=True)