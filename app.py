from flask import Flask, send_from_directory
import os

app = Flask(__name__)

# ==========================================
# DASHBOARD 1
# ==========================================
@app.route("/")
def loja1():
    return send_from_directory("dashboard", "FLV Loja 1.html")

# ==========================================
# DASHBOARD 2
# ==========================================
@app.route("/loja2")
def loja2():
    return send_from_directory("dashboard", "FLV Loja 2.html")

# ==========================================
# DASHBOARD 3
# ==========================================
@app.route("/loja3")
def loja3():
    return send_from_directory("dashboard", "FLV Loja 3.html")

# ==========================================
# SERVIDOR
# ==========================================
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)