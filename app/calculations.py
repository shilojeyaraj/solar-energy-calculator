import requests
import googlemaps

# Replace with your actual API keys
GOOGLE_API_KEY = "AIzaSyCYKcbRqRxAXlqWlhaUSCitcdfkmKe6T7w"  # Google Maps API key
NASA_API_KEY = "0jcKTihYP7ZMptmzCJFvqwIgKmkz3TyLJekQEkaa"  # NASA API key (optional, can be empty "")

# Initialize Google Maps client
gmaps = googlemaps.Client(key=GOOGLE_API_KEY)

def get_lat_lon(city):
    """Get latitude and longitude using Google Maps API."""
    try:
        geocode_result = gmaps.geocode(city)
        if geocode_result:
            location = geocode_result[0]['geometry']['location']
            return location['lat'], location['lng']
        else:
            return None, None
    except Exception as e:
        print(f"Error retrieving location: {e}")
        return None, None

def get_nasa_solar_irradiance(lat, lon, nasa_api_key):
    """Fetch solar irradiance data from NASA POWER API using an API key."""
    url = f"https://power.larc.nasa.gov/api/temporal/daily/point?parameters=ALLSKY_SFC_SW_DWN&latitude={lat}&longitude={lon}&format=JSON&start=2023&end=2023&community=RE"
    
    # Add API key if available
    if nasa_api_key:
        url += f"&api_key={nasa_api_key}"
    
    response = requests.get(url)
    
    print("NASA API Response:", response.text)  # Debugging line
    
    if response.status_code == 200:
        data = response.json()
        try:
            irradiance = data['properties']['parameter']['ALLSKY_SFC_SW_DWN']
            avg_irradiance = sum(irradiance.values()) / len(irradiance)  # kWh/m²/day
            return avg_irradiance * 1000  # Convert to Wh/m²/day
        except KeyError:
            print("Error: Could not find expected irradiance data in the response.")
            return None
    else:
        print(f"Error: NASA API request failed with status code {response.status_code}")
        return None

def calculate_solar_power(city, panel_area, panel_efficiency, nasa_api_key):
    """Calculate solar energy output."""
    # Get latitude & longitude
    lat, lon = get_lat_lon(city)
    if lat is None or lon is None:
        return None, "Error: City not found."

    # Get solar irradiance from NASA API
    irradiance = get_nasa_solar_irradiance(lat, lon, nasa_api_key)
    if irradiance is None:
        return None, "Error: Failed to retrieve solar irradiance data from NASA."

    # Energy calculation
    hours_of_sunlight = 5  # Assume 5 peak sun hours
    power_output = irradiance * panel_area * panel_efficiency / 100  # Wh/day
    daily_energy_output = power_output * hours_of_sunlight  # Wh/day
    annual_energy_output = daily_energy_output * 365  # Wh/year

    results = {
        'latitude': lat,
        'longitude': lon,
        'irradiance': irradiance,
        'energy_output': daily_energy_output,
        'annual_energy_output': annual_energy_output
    }

    return results, None