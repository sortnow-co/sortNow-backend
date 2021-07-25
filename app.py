from flask import Flask, jsonify

app = Flask(__name__)

app.config["SECRET_KEY"] = "alvbnskbvk28er20tyrc"


@app.route("/", methods=["GET"])
def index():
    return jsonify("Welcome to sortNow")


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)
