from flask import Flask, render_template
import random
import platform

app = Flask(__name__)

# list of gif images
images = [
    "https://media.giphy.com/media/11sBLVxNs7v6WA/giphy.gif",
    "https://media.giphy.com/media/l4pT0zpKP6rv4JdgQ/giphy.gif",
    "https://media.giphy.com/media/dMYVHzANYb9p6/giphy.gif",
    "https://media.giphy.com/media/1yYWGu3caE3m0/giphy.gif",
    "https://media.giphy.com/media/uH7JevzEbPl1m/giphy.gif",
    "https://media.giphy.com/media/YqTzLj0Vzct9K/giphy.gif",
    "https://media.giphy.com/media/6CMfEkZd41ZtK/giphy.gif",
    "https://media.giphy.com/media/2xUfwmis1bpwA/giphy.gif",
    "https://media.giphy.com/media/TxZBMKYYpN7m8/giphy.gif",
    "https://media.giphy.com/media/MOWPkhRAUbR7i/giphy.gif"
]

@app.route('/')
def index():
    url = random.choice(images)
    hostname = platform.node()
    return render_template('index.html', url=url, hostname=hostname)

if __name__ == "__main__":
    app.run(host="0.0.0.0")
