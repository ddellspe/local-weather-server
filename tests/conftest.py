from __future__ import annotations

import contextlib
import os.path
import sqlite3
from typing import NamedTuple

import pytest

from local_weather_server.server.app import create_schema_sqlite


@pytest.fixture
def tempdir_factory(tmpdir):
    class TmpdirFactory:
        def __init__(self):
            self.tmpdir_count = 0

        def get(self):
            path = tmpdir.join(str(self.tmpdir_count)).strpath
            self.tmpdir_count += 1
            os.mkdir(path)
            return path

    yield TmpdirFactory()


class Sandbox(NamedTuple):
    directory: str

    @property
    def db_path(self):
        return os.path.join(self.directory, 'db.db')

    @contextlib.contextmanager
    def db(self):
        with sqlite3.connect(self.db_path) as db:
            yield db


@pytest.fixture
def sandbox(tempdir_factory):
    ret = Sandbox(tempdir_factory.get())
    with ret.db() as db:
        create_schema_sqlite(db)

    yield ret
