import base64
import logging
import requests

from api.networks import base
from api.errors import exceptions
from api.responses import twitter


class Twitter(base.NetworkBase):

    def __init__(self):
        self.bearer_token = None

        # individual values in case the base string is needed
        self.consumer_key = "CZJqTZeJFRrJuT3yfZpl5zDlo"
        self.consumer_secret = (
            "GCwM9ftx3MfJ2l1rYvhYcKlUPDsWSOxaZ7r8WGHmnQg4C3Ho9M"
        )

        self.encoded_token = base64.b64encode(
            "{0}:{1}".format(self.consumer_key, self.consumer_secret)
        )

    def request_token(self):

        # token remains valid until invalidated
        # twitter will return same token
        if self.bearer_token:
            return

        # expected headers, would add to base. Headers can vary
        headers = {
            "Authorization": "Basic {0}".format(self.encoded_token),
            "User-Agent": "Waldo v.0.0.1",
        }

        # request bearer token
        resp = requests.post(
            url=(
                "https://api.twitter.com/oauth2/token?" +
                "grant_type=client_credentials"
            ),
            headers=headers
        )

        if resp.status_code is not 200:
            raise exceptions.TwitterException(resp)

        # set bearer_token for use
        self.bearer_token = resp.json()['access_token']
        logging.debug("Access token acquired")

    def invalidate_token(self):
        if self.bearer_token:

            headers = {
                "Authorization": "Basic {0}".format(self.encoded_token),
                "User-Agent": "Waldo v.0.0.1",
            }

            # invalidate the token
            resp = requests.post(
                url="https://api.twitter.com/oauth2/token?" +
                "grant_type=client_credentials",
                headers=headers
            )

            if resp.status_code is not 200:
                raise exceptions.TwitterException(resp)

            self.bearer_token = None
            logging.debug("Token invalidated")

    def get_feed(self, query, lat=None, lng=None):
        if not self.bearer_token:
            raise exceptions.NoBearerToken()

        headers = {
            "Authorization": "Bearer {0}".format(self.bearer_token)
        }

        resp = requests.get(
            url="https://api.twitter.com/1.1/search/tweets.json?q={0}".format(
                str(query)
            ),
            headers=headers
        )

        if resp.status_code is not 200 or "error" in resp.json():
            raise exceptions.TwitterException(resp)

        return twitter.TwitterResponse(resp.json()['statuses'])
