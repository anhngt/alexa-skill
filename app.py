# !flask/bin/python
from flask import Flask, jsonify

app = Flask(__name__)
from flask import Flask
from flask import request

app = Flask(__name__)

response = {
    'version': '1.0',
    'sessionAttributes': {},
    'response': {
        'outputSpeech': {
            'type': 'PlainText',
            'text': 'There are 3 atm'
        },
        'shouldEndSession': True
    }
}


@app.route('/', methods=['POST'])
def post():
    print(request.is_json)
    content = request.get_json()
    print(content)

    return jsonify(response)


app.run(host='0.0.0.0', port=5000)
