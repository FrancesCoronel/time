from flask import Flask
import time

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', time=epochTime())

def epochTime():
    return '<h1>' + str(int(time.time())) + '</h1>'

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)