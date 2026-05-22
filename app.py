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

    file=request.files["image"]

    input_data=file.read()

    output=remove(input_data)

    return send_file(
        io.BytesIO(output),
        mimetype="image/png"
    )


if __name__=="__main__":

    import os

    port=int(os.environ.get("PORT",10000))

    app.run(
        host="0.0.0.0",
        port=port,
        debug=False
    )
