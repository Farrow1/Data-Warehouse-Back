from flask import Flask


app = Flask(__name__)

@app.route('/test', methods=['GET'])
def defaultone():
    return "Loren ipsum dolor sit amet"

if __name__ == '__main__':
    app.run()