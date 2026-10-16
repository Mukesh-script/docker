
from flask import Flask
import redis
import os

app = Flask(__name__)

redis_client = redis.Redis(
    host=os.getenv("REDIS_HOST", "redis"),
    port=6379,
    decode_responses=True
)

@app.route("/")
def home():
    visits = redis_client.incr("visits")
    return f"""
    <h1>My Docker Application</h1>
    <p>Hello! My Python application is running.</p>
    <h2>Page visits: {visits}</h2>
    <p>Flask and Redis are running in separate containers.</p>
    """

@app.route("/health")
def health():
    return "Application is healthy!", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
