from flask import Flask, send_file
import os

app = Flask(__name__)

@app.route("/")
def dashboard():

    caminho = os.path.join(
        "dashboard",
        "FLV Loja 1.html"
    )

    return send_file(caminho)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)