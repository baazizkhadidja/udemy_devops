from flask import Flask, jsonify, request
from datetime import date

app = Flask(__name__)

@app.get("/health")
def health():
    return "ok", 200

@app.get("/")
def home():
    return "Student Age API is running"

@app.get("/age")
def age():
    """
    /age?year=2000&month=5&day=12
    """
    try:
        y = int(request.args.get("year"))
        m = int(request.args.get("month"))
        d = int(request.args.get("day"))
        born = date(y, m, d)
        today = date.today()
        years = today.year - born.year - ((today.month, today.day) < (born.month, born.day))
        return jsonify({"age": years})
    except Exception as e:
        return jsonify({"error": "Invalid or missing parameters", "detail": str(e)}), 400

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)