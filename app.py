from flask import Flask
import requests
import threading
import time
import logging

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)

# List of URLs to monitor
URLS = [
    "https://www.google.com",
    "https://www.github.com",
    "https://thisurldoesnotexist.xyz"
]

def monitor_urls():
    while True:
        for url in URLS:
            try:
                start = time.time()
                response = requests.get(url, timeout=5)
                latency = round((time.time() - start) * 1000, 2)  # in ms
                logging.info(f"[UP] {url} responded with {response.status_code} in {latency}ms")
            except requests.RequestException as e:
                logging.warning(f"[DOWN] {url} is unreachable - {e}")
        time.sleep(60)  # wait 60 seconds before next check

# Start the monitoring thread
threading.Thread(target=monitor_urls, daemon=True).start()

@app.route("/")
def home():
    return "URL Monitor is running."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
