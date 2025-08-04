from __future__ import annotations

import flask
from flask import request

from local_weather_server.models.database import WeatherData

wunderground = flask.Blueprint('wunderground', __name__)


@wunderground.route('/wunderground/import')
def import_weather_data() -> dict[str, str]:
    try:
        print(WeatherData.from_wungerground_request(**request.args))
    except TypeError:
        return {'message': 'failure'}
    return {'message': 'success'}
