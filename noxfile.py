# type: ignore
import os

import nox
from nox.sessions import Session

PROJECT_NAME = "oc_extras"

DEFAULT_PYTHON_VERSIONS = ["3.7", "3.8", "3.9"]

PYTHON_VERSIONS = os.environ.get(
    "NOX_PYTHON_VERSIONS", ",".join(DEFAULT_PYTHON_VERSIONS)
).split(",")


def setup(session: Session) -> None:
    session.install("--upgrade", "setuptools", "pip")
    session.install("-r", "requirements/dev.txt")


@nox.session(python=PYTHON_VERSIONS)
def lint(session: Session) -> None:
    setup(session=session)
    session.run("flake8", PROJECT_NAME)
    session.run("black", "--check", PROJECT_NAME)
    session.run("isort", PROJECT_NAME, "--check", "--diff")


@nox.session(python=PYTHON_VERSIONS)
def mypy(session: Session) -> None:
    setup(session=session)
    session.run("mypy", "--strict", PROJECT_NAME)
