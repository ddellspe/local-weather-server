from __future__ import annotations

import traceback

import flask
from flask import request

from local_weather_server.models.database import WeatherData
from local_weather_server.utils.db_utils import insert_weather_data

wunderground = flask.Blueprint('wunderground', __name__)


@wunderground.route('/wunderground/import')
def import_weather_data() -> dict[str, str]:
    try:
        data = WeatherData.from_wungerground_request(**request.args)
        insert_weather_data(db=flask.g.db, weather_data=data)
    except TypeError:
        traceback.print_exc()
        return {'message': 'failure'}
    return {'message': 'success'}
