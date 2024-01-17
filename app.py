from flask import Flask, redirect, request, render_template, url_for

# ./tailwindcss -i ./static/input.css -o ./static/output.css --watch
# ./tailwindcss -i ./static/input.css -o ./static/output.css --minify

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/map")
def map():
    return render_template("map.html")


if __name__ == '__main__':
    app.run(debug=True)
