from __future__ import annotations

import flask
from flask import request

from local_weather_server.models.database import WeatherData
from local_weather_server.utils.db_utils import insert_weather_data

awn = flask.Blueprint('awn', __name__)


@awn.route('/awn/import')
def import_weather_data() -> dict[str, str]:
    try:
        data = WeatherData.from_awn_request(**request.args)
        insert_weather_data(db=flask.g.db, weather_data=data)
    except TypeError:
        return {'message': 'failure'}
    return {'message': 'success'}
