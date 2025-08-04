from __future__ import annotations

import argparse
from collections.abc import Sequence
from typing import NoReturn

import flask

from local_weather_server.server.servlets.wunderground import wunderground

app = flask.Flask('local weather server')
app.register_blueprint(wunderground)


def main(argv: Sequence[str] | None = None) -> NoReturn:
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--port', type=int, default=5000)
    parser.add_argument(
        '--debug', action='store_true',
        help=(
            'Run in debug mode (stacktraces + single process). '
            'Not suggested for production.'
        ),
    )
    args = parser.parse_args(argv)

    kwargs = {'port': args.port, 'debug': args.debug}

    app.run('0.0.0.0', **kwargs)
    raise SystemExit(1)


if __name__ == '__main__':
    raise SystemExit(main())
