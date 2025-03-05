from datetime import datetime
import os
import shutil
import tempfile

from lektor import db
from lektor.builder import Builder
from lektor.environment import Environment
from lektor.project import Project
from lektor.reporter import BufferReporter
from lektor.types import Type
import pytest


class DatetimeType(Type):
    def value_from_raw(self, raw):
        return datetime.strptime(raw.value, "%Y-%m-%d %H:%M:%S")


@pytest.fixture(scope="function")
def project(request):
    return Project.from_path(os.path.join(os.path.dirname(__file__), "demo-project"))


@pytest.fixture(scope="function")
def env(request, project):
    e = Environment(project)
    e.types["datetime"] = DatetimeType  # As if we had a datetime plugin.
    return e


@pytest.fixture(scope="function")
def pad(request, env):
    return db.Database(env).new_pad()


def make_builder(request, pad):
    out = tempfile.mkdtemp()
    b = Builder(pad, out)

    def cleanup():
        try:
            shutil.rmtree(out)
        except OSError:
            pass

    request.addfinalizer(cleanup)
    return b


@pytest.fixture(scope="function")
def builder(request, pad):
    return make_builder(request, pad)


@pytest.fixture(scope="function")
def F():  # pylint: disable=invalid-name
    return db.F


@pytest.fixture(scope="function")
def reporter(request, env):
    r = BufferReporter(env)
    r.push()
    request.addfinalizer(r.pop)
    return r
