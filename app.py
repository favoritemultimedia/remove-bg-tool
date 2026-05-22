from flask import Flask, render_template, request, send_file
from rembg import remove
from PIL import Image
import io

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/remove", methods=["POST"])
def remove_bg():

    if "image" not in request.files:
        return "No image"

    file = request.files["image"]

    input_bytes = file.read()

    output = remove(input_bytes)

    return send_file(
        io.BytesIO(output),
        mimetype="image/png",
        as_attachment=False
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)