from flask import Flask, jsonify, request
#import requests
app = Flask(__name__)
@app.route('/', methods=['POST'])
def demo():
    json_form = request.get_json()
    return jsonify(json_form)


if __name__ == '__main__':
    app.run(port=4000, debug=True)
