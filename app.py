from flask import Flask
from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)
metrics = PrometheusMetrics(app)  # <-- enables /metrics

@app.route("/")
def Hello():
    return "Hello World"

@app.route("/new")
def new():
    return "Testing CI"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

