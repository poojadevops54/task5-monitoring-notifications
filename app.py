from flask import Flask
import logging
import os

app = Flask(__name__)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s"
)

@app.route("/")
def home():
    app.logger.info("Home page accessed")
    return "Task 5 Monitoring Application is Running!", 200

@app.route("/health")
def health():
    app.logger.info("Health check successful")
    return {"status": "healthy"}, 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
