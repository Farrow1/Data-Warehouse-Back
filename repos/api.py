from flask import Flask
from db_repos import default

app = Flask(__name__)

@app.route('/')
def defaultone():
    return default()

if __name__ == '__main__':
    app.run()