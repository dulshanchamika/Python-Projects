import requests
from flask import Flask, request, render_template

app = Flask(__name__)

# Function to get location from ipinfo.io API
def get_location_from_ip(ip_address=None):
    url = f"http://ipinfo.io/{ip_address}/json" if ip_address else "http://ipinfo.io/json"
    response = requests.get(url)
    data = response.json()

    print("API Response:", data)  # Debug: Print the raw response

    if response.status_code == 200:
        loc = data.get('loc')
        if loc:
            location = loc.split(',')
            return {
                "city": data.get('city', 'Unknown'),
                "region": data.get('region', 'Unknown'),
                "country": data.get('country', 'Unknown'),
                "latitude": location[0],
                "longitude": location[1]
            }
        else:
            return {"error": "Location not available"}
    else:
        return {"error": f"API error: {response.status_code}"}

@app.route('/')
def index():
    ip_address = request.remote_addr
    print(f"Client IP Address: {ip_address}")  # Debug: Print the IP address
    location = get_location_from_ip(ip_address)
    print("Location Data:", location)  # Debug: Print the location data
    return render_template('index.html', location=location)

if __name__ == '__main__':
    app.run(debug=True)
