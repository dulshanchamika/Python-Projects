import phonenumbers
from phonenumbers import geocoder, carrier
import folium
from opencage.geocoder import OpenCageGeocode

# Replace with your actual phone number (with country code)
number = "+"  # Example number

# Step 1: Parse the phone number
parsed_number = phonenumbers.parse(number)

# Step 2: Get the general location (country or region)
your_location = geocoder.description_for_number(parsed_number, "en")
print(f"Approximate Location: {your_location}")

# Step 3: Get the service provider (carrier)
service_provider = carrier.name_for_number(parsed_number, "en")
print(f"Service Provider: {service_provider}")

# Step 4: Use OpenCage Geocode API to get coordinates for the location
API_KEY = "9e9cb7b63ef24e51960d93a16b6ad555"  # Replace with your OpenCage API key
geocoder = OpenCageGeocode(API_KEY)
query = str(your_location)
results = geocoder.geocode(query)

# Check if results are available
if results:
    lat = results[0]['geometry']['lat']
    lng = results[0]['geometry']['lng']
    print(f"Latitude: {lat}, Longitude: {lng}")

    # Step 5: Create a map using folium
    my_map = folium.Map(location=[lat, lng], zoom_start=9)
    folium.Marker([lat, lng], popup=f"Location: {your_location}").add_to(my_map)

    # Step 6: Save the map to an HTML file
    my_map.save("phone_number_location.html")
    print("Map saved as 'phone_number_location.html'. Open it in a browser to view.")
else:
    print("Could not find coordinates for the given location.")
