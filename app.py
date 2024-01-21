from flask import Flask, render_template, request, jsonify, redirect

from map import get_user_location, get_nearby_spots

# ./tailwindcss -i ./static/input.css -o ./static/output.css --watch
# ./tailwindcss -i ./static/input.css -o ./static/output.css --minify

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/map')
def map():

    return render_template("map1.html")

@app.route('/birding_area', methods=["POST"])
def get_birding_area():
    user_location = request.json['userLocation']
    #print(user_location)
    birding_area = get_nearby_spots(location=user_location, radius=10000)
    #birding_area = {'html_attributions': [], 'results': [{'business_status': 'OPERATIONAL', 'geometry': {'location': {'lat': 1.2820075, 'lng': 103.867737}, 'viewport': {'northeast': {'lat': 1.283357329892722, 'lng': 103.8690868298927}, 'southwest': {'lat': 1.280657670107278, 'lng': 103.8663871701073}}}, 'icon': 'https://maps.gstatic.com/mapfiles/place_api/icons/v1/png_71/park-71.png', 'icon_background_color': '#4DB546', 'icon_mask_base_uri': 'https://maps.gstatic.com/mapfiles/place_api/icons/v2/tree_pinlet', 'name': 'Kingfisher Wetlands Wildlife Lookout', 'opening_hours': {'open_now': False}, 'photos': [{'height': 2268, 'html_attributions': ['<a href="https://maps.google.com/maps/contrib/104390192454543708691">EasyEasy Song</a>'], 'photo_reference': 'AWU5eFhss3MiYW3SDscI7a9F0ZH3yK8aP4aBgeE6MqluRsxT6veQAa2XbDggqREgoYkvOchH0uNLH4V3ZRaaxjh8eDXBqsPgJGBKY7QiAomTE0CMF2_9ktYT7XQ5SqbqPRl2z9VZFnJT9xT6E4MedgWdvS7MSO14wjGw5IIA0sTgY3mt5cUQ', 'width': 4032}], 'place_id': 'ChIJtfU3zT0Z2jER6lrC-S-Tw2U', 'plus_code': {'compound_code': '7VJ9+R3 Singapore', 'global_code': '6PH57VJ9+R3'}, 'rating': 4.7, 'reference': 'ChIJtfU3zT0Z2jER6lrC-S-Tw2U', 'scope': 'GOOGLE', 'types': ['park', 'point_of_interest', 'establishment'], 'user_ratings_total': 33, 'vicinity': 'Singapore'}, {'business_status': 'OPERATIONAL', 'geometry': {'location': {'lat': 1.3587991, 'lng': 103.8445142}, 'viewport': {'northeast': {'lat': 1.360188379892722, 'lng': 103.8458974798927}, 'southwest': {'lat': 1.357488720107278, 'lng': 103.8431978201073}}}, 'icon': 'https://maps.gstatic.com/mapfiles/place_api/icons/v1/png_71/park-71.png', 'icon_background_color': '#4DB546', 'icon_mask_base_uri': 'https://maps.gstatic.com/mapfiles/place_api/icons/v2/tree_pinlet', 'name': 'Bishan North Bird Pergola', 'photos': [{'height': 808, 'html_attributions': ['<a href="https://maps.google.com/maps/contrib/115680102960193169110">Adam Lee</a>'], 'photo_reference': 'AWU5eFh3b7dhYfUMmglG5ZGtwjWwVES-f--15VAePUZ0hFJkR5lZJy3OZCuwJpb_qFH0Khg3DlbB43vw5DGIpSYW83S2ZoLKpQ6dHU35e1kZ2pSxxXivUEkj5IkJt8bUdcV9czsg-FjeO1rSFBvC0PyQ88IKFnQYGUvy4uWnlQ3HuEAwwu4r', 'width': 1077}], 'place_id': 'ChIJ_RbRqRMX2jER3kZglUiB71Y', 'plus_code': {'compound_code': '9R5V+GR Singapore', 'global_code': '6PH59R5V+GR'}, 'rating': 5, 'reference': 'ChIJ_RbRqRMX2jER3kZglUiB71Y', 'scope': 'GOOGLE', 'types': ['park', 'point_of_interest', 'establishment'], 'user_ratings_total': 2, 'vicinity': '284 Bishan Street 22, Singapore'}, {'business_status': 'OPERATIONAL', 'geometry': {'location': {'lat': 1.3674994, 'lng': 103.8968994}, 'viewport': {'northeast': {'lat': 1.368684829892722, 'lng': 103.8980441798927}, 'southwest': {'lat': 1.365985170107278, 'lng': 103.8953445201073}}}, 'icon': 'https://maps.gstatic.com/mapfiles/place_api/icons/v1/png_71/park-71.png', 'icon_background_color': '#4DB546', 'icon_mask_base_uri': 'https://maps.gstatic.com/mapfiles/place_api/icons/v2/tree_pinlet', 'name': 'Bird Singing Corner (Hougang Ave 5)', 'photos': [{'height': 4000, 'html_attributions': ['<a href="https://maps.google.com/maps/contrib/106288525842576512037">Ahmad Akram Mohamed Ismail</a>'], 'photo_reference': 'AWU5eFh7f9aDEv-iq-BeBcgjN0DdGKxUllVYlpsO7MUbqPhZdZ2tVUnwc7GXdz55Xpf3H-5uOIM053VTOfzRhGeYH8JVadXcUQQF80rNvT3VR6KqKkI695TfANPTiP0wbXTZrRkBoYmDFwywPNar3FDGEB8jRehqRieYvomrSsN7wRcZkYBu', 'width': 2252}], 'place_id': 'ChIJH7KqlQwX2jERBN4e96pi-UQ', 'plus_code': {'compound_code': '9V8W+XQ Singapore', 'global_code': '6PH59V8W+XQ'}, 'rating': 0, 'reference': 'ChIJH7KqlQwX2jERBN4e96pi-UQ', 'scope': 'GOOGLE', 'types': ['park', 'point_of_interest', 'establishment'], 'user_ratings_total': 0, 'vicinity': '324 Hougang Ave 5, Block 324, Singapore'}, {'business_status': 'OPERATIONAL', 'geometry': {'location': {'lat': 1.3743283, 'lng': 103.8402746}, 'viewport': {'northeast': {'lat': 1.375701929892722, 'lng': 103.8416212798927}, 'southwest': {'lat': 1.373002270107278, 'lng': 103.8389216201073}}}, 'icon': 'https://maps.gstatic.com/mapfiles/place_api/icons/v1/png_71/park-71.png', 'icon_background_color': '#4DB546', 'icon_mask_base_uri': 'https://maps.gstatic.com/mapfiles/place_api/icons/v2/tree_pinlet', 'name': 'Kebun Baru Birdsinging Club', 'opening_hours': {'open_now': False}, 'photos': [{'height': 3024, 'html_attributions': ['<a href="https://maps.google.com/maps/contrib/107810333428319776700">A Google User</a>'], 'photo_reference': 'AWU5eFi00WLgA3ydu-MYT7hlc7n0g6P9xyV7NqJZh6xqQzYx-rdlwwktw9oCNN6WLw0U5l5q0KKUfdHXGnD9C6b_7rTZ3VJGeBcgO7pLgsA09qDwYxbt4JznDGKoP1cZronuElYkE9gBb9doMDjWkZWc_GgvFz719QSU_-oigCLBF6rPKQJE', 'width': 4032}], 'place_id': 'ChIJp_EOScIW2jEROzizxCwnfQk', 'plus_code': {'compound_code': '9RFR+P4 Singapore', 'global_code': '6PH59RFR+P4'}, 'rating': 4.3, 'reference': 'ChIJp_EOScIW2jEROzizxCwnfQk', 'scope': 'GOOGLE', 'types': ['tourist_attraction', 'park', 'point_of_interest', 'establishment'], 'user_ratings_total': 139, 'vicinity': 'Block 159 Ang Mo Kio Ave 5, Singapore'}, {'business_status': 'OPERATIONAL', 'geometry': {'location': {'lat': 1.3133218, 'lng': 103.7626408}, 'viewport': {'northeast': {'lat': 1.314761429892722, 'lng': 103.7639912298927}, 'southwest': {'lat': 1.312061770107278, 'lng': 103.7612915701073}}}, 'icon': 'https://maps.gstatic.com/mapfiles/place_api/icons/v1/png_71/park-71.png', 'icon_background_color': '#4DB546', 'icon_mask_base_uri': 'https://maps.gstatic.com/mapfiles/place_api/icons/v2/tree_pinlet', 'name': 'Bird Singing Hangout', 'photos': [{'height': 3024, 'html_attributions': ['<a href="https://maps.google.com/maps/contrib/111508052288518804128">Tan Choon Heong</a>'], 'photo_reference': 'AWU5eFhBtIEl1uUn25BOsKe1ghBuiwP9KoDR0SWIbHAoJLCIBeBFzdUr-dNB1SUZFuMCVevGpryGf2OvXE9IvClnQ2qRzyhTO9IK-oy_Ho2bhTRY-75pvRgV0gkRsT8bT_ZINQSV-TbYb17XOnJKpjgQU2DZWE1TssHc1UrCtw-ZTqirvKDL', 'width': 4032}], 'place_id': 'ChIJ76wX31kb2jERfvB3xs0qkZs', 'plus_code': {'compound_code': '8Q77+83 Singapore', 'global_code': '6PH58Q77+83'}, 'rating': 5, 'reference': 'ChIJ76wX31kb2jERfvB3xs0qkZs', 'scope': 'GOOGLE', 'types': ['park', 'point_of_interest', 'establishment'], 'user_ratings_total': 1, 'vicinity': '430 Clementi Ave 3, Block 430, Singapore'}, {'business_status': 'OPERATIONAL', 'geometry': {'location': {'lat': 1.2751151, 'lng': 103.8265277}, 'viewport': {'northeast': {'lat': 1.276466129892722, 'lng': 103.8278281298927}, 'southwest': {'lat': 1.273766470107278, 'lng': 103.8251284701073}}}, 'icon': 'https://maps.gstatic.com/mapfiles/place_api/icons/v1/png_71/park-71.png', 'icon_background_color': '#4DB546', 'icon_mask_base_uri': 'https://maps.gstatic.com/mapfiles/place_api/icons/v2/tree_pinlet', 'name': '武吉宝美鸟廊 Bukit Purmei Bird Arena', 'photos': [{'height': 3024, 'html_attributions': ['<a href="https://maps.google.com/maps/contrib/111316266362121177513">shuan fey lee</a>'], 'photo_reference': 'AWU5eFjfMVthYCeIq6rH6G4VwaJ44rid-1_Kgjq1n1w5PlA_j7b9eypBQ9Zrk_FgXeV-XWQiDGQHimQHOPsh7hl_5l5WIKs6Xg4szgp8gwIT1i61xgz-T5VcS-UTVJQSul6k2ckg0LMUmEAvMbo0ixapmtghdQwYzwF6iIkiDmnuLUwBLZyZ', 'width': 4032}], 'place_id': 'ChIJ-SZS-4YZ2jERKzfhGwj9XOE', 'plus_code': {'compound_code': '7RGG+2J Singapore', 'global_code': '6PH57RGG+2J'}, 'rating': 3, 'reference': 'ChIJ-SZS-4YZ2jERKzfhGwj9XOE', 'scope': 'GOOGLE', 'types': ['park', 'point_of_interest', 'establishment'], 'user_ratings_total': 1, 'vicinity': 'Bukit Purmei Rd, Block 115, Singapore'}], 'status': 'OK'}
    #print(birding_area)

    return jsonify({'birding_area' : birding_area})

#@app.rout('/test', methods=['POST'])

if __name__ == '__main__':
    app.run(debug=True)
