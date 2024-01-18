import googlemaps


def get_user_location(api_key):
    # Initialize the Google Maps client
    gmaps = googlemaps.Client(key=api_key)

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


def get_nearby_birdwatching_spots(api_key, location, radius=5000, keyword="birdwatching area"):
    # Initialize the Google Maps client
    gmaps = googlemaps.Client(key=api_key)

    try:
        # Search for nearby places with the specified keyword (e.g., "bird watching")
        places_result = gmaps.places_nearby(
            location=location,
            radius=radius,
            keyword=keyword
        )
        # Extract relevant information
        nearby_spots = []

        for place in places_result["results"]:
            name = place.get("name", "N/A")
            address = place.get("vicinity", "N/A")
            rating = place.get("rating", "N/A")
            location = place.get("geometry").get("location")
            lat = location.get("lat")
            lng = location.get("lng")
            nearby_spots.append({
                "name": name,
                "address": address,
                "rating": rating,
                "lat": lat,
                "lng": lng
            })

        return nearby_spots

    except googlemaps.exceptions.ApiError as e:
        print(f"Error: {e}")
        return None


# Replace 'YOUR_GOOGLE_MAPS_API_KEY' with your actual API key
api_key = 'AIzaSyBVaeNch_aeLuTOIVX75orHHF0z7eeGlJI'

# Get user's location
user_location = get_user_location(api_key)

if user_location:
    print(f"User Location: {user_location}")

    # Get nearby bird watching spots
    nearby_spots = get_nearby_birdwatching_spots(api_key, user_location)

    if nearby_spots:
        print("\nNearby Bird Watching Spots:")
        for spot in nearby_spots:
            print(f"Name: {spot['name']}, Address: {spot['address']}, Rating: {spot['rating']}")
    else:
        print("Unable to retrieve nearby bird watching spots.")
else:
    print("Unable to retrieve user location.")
