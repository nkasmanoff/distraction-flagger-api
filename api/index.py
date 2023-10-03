from flask import Flask, request
from flask_cors import CORS
import pickle



app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return 'Distraction flagger backend. Check out the /check-distraction endpoint to see what this returns'

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
    # pass the input and topic to the model

    output = check_relevance(_input)

    # return the output as a json object
    return {'result': output}



def check_relevance(_input):
    """
    Simple rule based approach for checking if a webpage is on topic or not. 

    Gets the word overlap between the input and topic. 
    
    If there is at least one word from the topic in the input, returns 0. Otherwise, returns 1
    
    """

    model = pickle.load(open('api/focus_model.pkl', 'rb'))
    tfidf = pickle.load(open('api/tfidf.pkl', 'rb'))
    prediction = model.predict(tfidf.transform([_input]))
    print("prediction: ", prediction)
    return prediction[0]
