from flask import Flask, render_template, request
import googlemaps

app = Flask(__name__)

# Initialize Google Maps client with your API key
API_KEY = 'AIzaSyCu4cPgsCXjhg9Ez_HHKudv37VKdOt20WU'  # Replace with your actual API key
gmaps = googlemaps.Client(key=API_KEY)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_directions', methods=['POST'])
def get_directions():
    origin = request.form['origin']
    destination = request.form['destination']
    
    try:
        # Get directions from Google Maps API
        directions = gmaps.directions(origin, destination)
        return {'directions': directions}
    except Exception as e:
        return {'error': str(e)}

@app.route('/geocode', methods=['POST'])
def geocode():
    address = request.form['address']
    
    try:
        # Geocode the address using Google Maps API
        geocode_result = gmaps.geocode(address)
        return {'geocode_result': geocode_result}
    except Exception as e:
        return {'error': str(e)}

@app.route('/places', methods=['POST'])
def places():
    location = request.form['location']  # Example format: "21.1458,79.0882"
    
    try:
        # Find nearby places using Google Maps Places API
        places_result = gmaps.places_nearby(location=location, radius=1000)
        return {'places_result': places_result}
    except Exception as e:
        return {'error': str(e)}

if __name__ == '__main__':
    app.run(debug=True)
