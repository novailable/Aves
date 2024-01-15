from flask import Flask, redirect, request, render_template, url_for


#./tailwindcss -i ./static/input.css -o ./static/output.css --watch
#./tailwindcss -i static/input.css -o static/output.css --minify

app = Flask(__name__)


@app.route("/")
def get_index():
    return render_template("index.html")


if __name__ == '__main__':
    app.run(debug=True)
