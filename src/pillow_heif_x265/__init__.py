"""Provide all possible stuff that can be used."""

from ._version import __version__


def get_path() -> str:
    """Returns the absolute path to the C extension that is the ``libheif`` plugin."""
    from . import _x265

    return _x265.__file__
