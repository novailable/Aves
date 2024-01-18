import googlemaps

gmaps = googlemaps.Client(key="AIzaSyBVaeNch_aeLuTOIVX75orHHF0z7eeGlJI")

def get_user_location():
    # Initialize the Google Maps client
    try:
        # Retrieve the user's location based on their IP address
        location_data = gmaps.geolocate()

        # Extract relevant information
        latitude = location_data["location"]["lat"]
        longitude = location_data["location"]["lng"]

        return latitude, longitude

    except googlemaps.exceptions.ApiError as e:
        print(f"Error: {e}")
        return None

def birdwatching_area():
    lat, lon = get_user_location()
    user_location = (lat, lon)

    # Fetch birdwatching locations near the user
    birdwatching_places = gmaps.places_nearby(location=user_location, radius=5000, type="birdwatching")

    # Prepare dictionary for template rendering
    map_data = {
        "markers": [place["geometry"]["location"] for place in birdwatching_places["results"]],
        "center": user_location,
        "zoom_level": 12,
    }

    return map_data

if __name__ == '__main__':
    lat, lon = get_user_location()
    print(lat, lon)