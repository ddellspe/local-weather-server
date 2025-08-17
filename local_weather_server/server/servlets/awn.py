from __future__ import annotations

import flask
from flask import request

from local_weather_server.models.database import WeatherData

awn = flask.Blueprint('awn', __name__)


@awn.route('/awn/import')
def import_weather_data() -> dict[str, str]:
    try:
        print(WeatherData.from_awn_request(**request.args))
    except TypeError:
        return {'message': 'failure'}
    return {'message': 'success'}
