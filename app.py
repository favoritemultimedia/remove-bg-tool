from flask import Flask, render_template, request, send_file
from rembg import remove
import io
import os

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/remove", methods=["POST"])
def remove_bg():

    if "image" not in request.files:
        return "No file",400

    file=request.files["image"]

    output=remove(file.read())

    return send_file(
        io.BytesIO(output),
        mimetype="image/png"
    )


port=int(os.environ.get("PORT",10000))

app.run(
    host="0.0.0.0",
    port=port
)
