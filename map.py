import googlemaps



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

class geo_map():

    def __init__(self):
        self.__API = "AIzaSyBVaeNch_aeLuTOIVX75orHHF0z7eeGlJI"
        self.__gmaps = googlemaps.Client(key=self.__API)
        self.__map_id = '16d8ab4a81eec419'

    def get_API_ID(self):
        return self.__API, self.__map_id

    def get_nearby_spots(self, location, radius, keyword="birdwatching area"):
        # Initialize the Google Maps client
        self.location = location
        self.radius = radius
        self.keyword = keyword

        try:
            # Search for nearby places with the specified keyword (e.g., "bird watching")
            places_result = self.__gmaps.places_nearby(
                location=self.location,
                radius=self.radius,
                keyword=self.keyword
            )

            nearby_spots = []
            for place in places_result["results"]:
                nearby_spots.append({
                    "name": place.get("name", "N/A"),
                    "address": place.get("vicinity", "N/A"),
                    "rating": place.get("rating", "N/A"),
                    "location": place.get("geometry").get("location")
                })

            return places_result

        except googlemaps.exceptions.ApiError as e:
            print(f"Error: {e}")
            return None
