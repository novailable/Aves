from flask import Flask, render_template

from map import get_user_location, get_nearby_spots

# ./tailwindcss -i ./static/input.css -o ./static/output.css --watch
# ./tailwindcss -i ./static/input.css -o ./static/output.css --minify

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/map")
def map():
    user_location = get_user_location()
    print("user<", user_location)
    print(get_nearby_spots(user_location, 10000))
    return render_template("map1.html",
                           user_location=get_user_location(),
                           birding_area=get_nearby_spots(location=user_location, radius=10000,
                                                         keyword="Bird watching area"))


if __name__ == '__main__':
    app.run(debug=True)
