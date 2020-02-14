from flask import Flask


app = Flask(__name__)

@app.route('/')
def test():
    return "Loren ipsum dolor sit amet"

if __name__ == '__main__':
    app.run()