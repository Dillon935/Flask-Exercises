from datetime import datetime
from flask import Flask
app = Flask(__name__)

@app.route("/")
def index():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    return f"Current time is {current_time}"

if __name__ == '__main__':
    app.run(debug=True)