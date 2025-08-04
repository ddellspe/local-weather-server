from __future__ import annotations

import flask


def _test_call_wundergound(server, query_params=None):
    return server.client.get(
        flask.url_for('wunderground.import_weather_data'),
        query_string=query_params,
    )


def test_it_returns_failure_with_wrong_query_parameters(server):
    resp = _test_call_wundergound(server)
    assert resp.json == {'message': 'failure'}


def test_it_returns_success_with_correct_query_parameters_now_utc(server):
    resp = _test_call_wundergound(
        server,
        {
            'ID': 'Identifier',
            'dateutc': 'now',
            'tempf': '70.0',
            'humidity': '70.0',
            'winddir': '120',
            'windgustmph': '5.0',
            'windspeedmph': '130',
            'rainin': '0.01',
            'dailyrainin': '0.02',
            'weeklyrainin': '0.04',
            'monthlyrainin': '0.10',
            'yearlyrainin': '0.50',
            'solarradiation': '450.5',
            'UV': '2',
            'absbaromin': '29.98',
            'baromin': '29.99',
        },
    )
    assert resp.json == {'message': 'success'}


def test_it_returns_success_with_correct_query_parameters_set_date(server):
    resp = _test_call_wundergound(
        server,
        {
            'ID': 'Identifier',
            'dateutc': '2025-05-05 12:00:35',
            'tempf': '70.0',
            'humidity': '70.0',
            'winddir': '120',
            'windgustmph': '5.0',
            'windspeedmph': '130',
            'rainin': '0.01',
            'dailyrainin': '0.02',
            'weeklyrainin': '0.04',
            'monthlyrainin': '0.10',
            'yearlyrainin': '0.50',
            'solarradiation': '450.5',
            'UV': '2',
            'absbaromin': '29.98',
            'baromin': '29.99',
        },
    )
    assert resp.json == {'message': 'success'}
