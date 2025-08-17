from __future__ import annotations

import flask


def _test_call_awn(server, query_params=None):
    return server.client.get(
        flask.url_for('awn.import_weather_data'),
        query_string=query_params,
    )


def test_it_returns_failure_with_wrong_query_parameters(server):
    resp = _test_call_awn(server)
    assert resp.json == {'message': 'failure'}


def test_it_returns_success_with_correct_query_parameters_now_utc(server):
    resp = _test_call_awn(
        server,
        {
            'PASSKEY': 'Identifier',
            'dateutc': 'now',
            'tempf': '70.0',
            'humidity': '70.0',
            'winddir': '120',
            'windgustmph': '5.0',
            'windspeedmph': '130',
            'hourlyrainin': '0.01',
            'dailyrainin': '0.02',
            'weeklyrainin': '0.04',
            'monthlyrainin': '0.10',
            'yearlyrainin': '0.50',
            'solarradiation': '450.5',
            'uv': '2',
            'baromabsin': '29.98',
            'baromrelin': '29.99',
        },
    )
    assert resp.json == {'message': 'success'}


def test_it_returns_success_with_correct_query_parameters_set_date(server):
    resp = _test_call_awn(
        server,
        {
            'PASSKEY': 'Identifier',
            'dateutc': '2025-05-05 12:00:35',
            'tempf': '70.0',
            'humidity': '70.0',
            'winddir': '120',
            'windgustmph': '5.0',
            'windspeedmph': '130',
            'hourlyrainin': '0.01',
            'dailyrainin': '0.02',
            'weeklyrainin': '0.04',
            'monthlyrainin': '0.10',
            'yearlyrainin': '0.50',
            'solarradiation': '450.5',
            'uv': '2',
            'baromabsin': '29.98',
            'baromrelin': '29.99',
        },
    )
    assert resp.json == {'message': 'success'}
