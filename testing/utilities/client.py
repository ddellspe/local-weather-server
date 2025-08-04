from __future__ import annotations

import json

import flask.testing


class Response:

    def __init__(self, response):
        self.response = response

    @property
    def text(self):
        return self.response.text

    @property
    def json(self):
        return json.loads(self.text)


class Client(flask.testing.FlaskClient):

    def open(self, *args, **kwargs):
        return Response(super().open(*args, **kwargs))
