import googlemaps
from datetime import datetime

# Initialize the Google Maps client
gmaps = googlemaps.Client(key="AIzaSyCu4cPgsCXjhg9Ez_HHKudv37VKdOt20WU")

# 1. Geocoding API: Convert an address to lat/lng
address = "VNIT Nagpur"
geocode_result = gmaps.geocode(address)
lat_lng = geocode_result[0]['geometry']['location']
print(f"Geocoding Result for VNIT: {lat_lng}")

# 2. Distance Matrix API: Calculate travel time from VNIT to a location
origins = [(lat_lng['lat'], lat_lng['lng'])]
destinations = ["Nagpur Railway Station, Nagpur, India"]
distance_matrix_result = gmaps.distance_matrix(origins, destinations, mode="driving")
distance = distance_matrix_result['rows'][0]['elements'][0]['distance']['text']
duration = distance_matrix_result['rows'][0]['elements'][0]['duration']['text']
print(f"Distance from VNIT to Nagpur Railway Station: {distance}, Duration: {duration}")

# 3. Directions API: Get driving directions from VNIT to another place
directions_result = gmaps.directions("VNIT Nagpur",
                                     "Nagpur Railway Station",
                                     mode="driving",
                                     departure_time=datetime.now())
print(f"Directions Result: {directions_result[0]['summary']}")

# 4. Elevation API: Get the elevation of VNIT Nagpur
elevation_result = gmaps.elevation((lat_lng['lat'], lat_lng['lng']))
elevation = elevation_result[0]['elevation']
print(f"Elevation of VNIT Nagpur: {elevation} meters")

# Additional Feature: Display the map on a webpage (HTML with embedded Google Maps)
map_html = f"""
<!DOCTYPE html>
<html>
  <head>
    <title>Google Maps Embed</title>
    <script src="https://maps.googleapis.com/maps/api/js?key=AIzaSyCu4cPgsCXjhg9Ez_HHKudv37VKdOt20WU&callback=initMap" async defer></script>
    <style>#map {{ height: 100%; width: 100%; }}</style>
  </head>
  <body>
    <h3>Map Showing VNIT Nagpur</h3>
    <div id="map" style="height:400px;width:100%"></div>
    <script>
      function initMap() {{
        var vnitLocation = {{ lat: {lat_lng['lat']}, lng: {lat_lng['lng']} }};
        var map = new google.maps.Map(document.getElementById('map'), {{
          zoom: 15,
          center: vnitLocation
        }});
        var marker = new google.maps.Marker({{
          position: vnitLocation,
          map: map,
          title: 'VNIT Nagpur'
        }});
      }}
    </script>
  </body>
</html>
"""

# Save HTML to a file
with open("map_embed.html", "w") as file:
    file.write(map_html)
