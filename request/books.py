import requests
import json


def call(**kwargs):

    url = "https://www.googleapis.com/books/v1/volumes?"

    params = kwargs

    try:
        response = requests.get(url, params).json()

        return response

    except:
        Error = "API error during request"

        return Error
