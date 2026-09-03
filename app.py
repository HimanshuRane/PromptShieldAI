from flask import Flask, render_template, request, jsonify
from gemma import analyze_prompt

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/analyze", methods=["POST"])
def analyze():

    data = request.get_json()

    prompt = data.get("prompt", "").strip()

    if prompt == "":
        return jsonify({
            "error": "Prompt cannot be empty."
        }), 400

    result = analyze_prompt(prompt)

    return jsonify(result)


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )