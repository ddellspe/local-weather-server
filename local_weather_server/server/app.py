from __future__ import annotations

import argparse
import importlib
import os
import sqlite3
from collections.abc import Sequence
from typing import NoReturn

import flask

from local_weather_server.server.servlets.awn import awn
from local_weather_server.server.servlets.wunderground import wunderground

app = flask.Flask('local weather server')
app.register_blueprint(wunderground)
app.register_blueprint(awn)


class AppContext:
    database_path = 'database.db'


@app.before_request
def before_request() -> None:
    flask.g.db = sqlite3.connect(AppContext.database_path, autocommit=True)


@app.teardown_request
def teardown_request(_: object) -> None:
    flask.g.db.close()


def create_schema_sqlite(db: sqlite3.Connection) -> None:
    schema_dir = str(
        importlib.resources.files(
            'local_weather_server',
        ).joinpath('schema', 'sqlite'),
    )
    schema_files = os.listdir(schema_dir)

    for sql_file in schema_files:
        resource_filename = os.path.join(schema_dir, sql_file)
        with open(resource_filename) as resource:
            db.executescript(resource.read())


def create_database(database: str) -> None:
    with sqlite3.connect(database) as db:
        create_schema_sqlite(db)


def main(argv: Sequence[str] | None = None) -> NoReturn:
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--port', type=int, default=5000)
    parser.add_argument('-d', '--database', type=str, default='database.db')
    parser.add_argument(
        '--debug', action='store_true',
        help=(
            'Run in debug mode (stacktraces + single process). '
            'Not suggested for production.'
        ),
    )
    args = parser.parse_args(argv)

    if not os.path.exists(args.database):
        create_database(args.database)

    AppContext.database_path = args.database

    kwargs = {'port': args.port, 'debug': args.debug}

    app.run('0.0.0.0', **kwargs)
    raise SystemExit(1)


if __name__ == '__main__':
    raise SystemExit(main())
