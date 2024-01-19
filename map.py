import googlemaps

gmaps = googlemaps.Client(key="AIzaSyBVaeNch_aeLuTOIVX75orHHF0z7eeGlJI")


def get_user_location():
    # Initialize the Google Maps client
    try:
        # Retrieve the user's location based on their IP address
        location_data = gmaps.geolocate()
        # Extract relevant information
        location = location_data.get("location")
        return location

    except googlemaps.exceptions.ApiError as e:
        print(f"Error: {e}")
        return None


def get_nearby_spots(location, radius=10000, keyword="birdwatching area"):
    # Initialize the Google Maps client

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
            nearby_spots.append({
                "name": name,
                "address": address,
                "rating": rating,
                "location": location
            })

        return nearby_spots

    except googlemaps.exceptions.ApiError as e:
        print(f"Error: {e}")
        return None


if __name__ == '__main__':
    loc = get_user_location()
    lat = loc.get("lat")
    lng = loc.get("lng")
    map = get_nearby_spots(loc)
    for m in map:
        print(m)
