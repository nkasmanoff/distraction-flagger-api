from flask import Flask, request
from helpers import check_relevance
app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, World!'

@app.route('/about')
def about():
    return "This is a really simple API. It is used as the backend for a FireFox extension that checks if a webpage is on topic or not."


# create route called check_distraction which loads in the payload of input and topic and passes to a function
# function will return a json object with the output of the model
@app.route('/check-distraction', methods=['GET'])
def check_distraction():
    # get the input and topic from the request
    _input = request.args.get('input')
    if _input is None:
        return {'result':1}
    _topic = request.args.get('topic')

    # pass the input and topic to the model
    output = check_relevance(_input, _topic)

    # return the output as a json object
    return {'result': output}


