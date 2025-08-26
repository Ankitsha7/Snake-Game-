from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# super simple in-memory high score (resets when server restarts)
HIGH_SCORE = {"score": 0}

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/highscore", methods=["GET", "POST"])
def highscore():
    global HIGH_SCORE
    if request.method == "POST":
        data = request.get_json(silent=True) or {}
        score = int(data.get("score", 0))
        if score > HIGH_SCORE["score"]:
            HIGH_SCORE["score"] = score
        return jsonify(HIGH_SCORE)
    return jsonify(HIGH_SCORE)

if __name__ == "__main__":
    app.run(debug=True)
