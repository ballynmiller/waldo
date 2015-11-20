import flask
from flask.ext.cors import CORS
import logging

from api.errors import exceptions
from api.networks import twitter
from api.networks import wikipedia

app = flask.Flask(__name__)
CORS(app)


@app.route("/feeds/<query>", methods=['GET'])
def feeds(query):
    results = []
    try:
        twitter_connection = twitter.Twitter()
        twitter_connection.request_token()
        results += twitter_connection.get_feed(query).create_response()
    except exceptions.TwitterException, e:
        logging.debug(e)
        results += []

    try:
        wikipedia_connection = wikipedia.Wikipedia()
        results += wikipedia_connection.get_feed(query).create_response()
    except exceptions.WikipediaException, e:
        logging.debug(e)
        results += []

    return flask.jsonify({
        'feeds': results
    })


if __name__ == "__main__":
    app.run()
