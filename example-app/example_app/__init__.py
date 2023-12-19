# These three lines comes from versioneer.
# Add to this file if you want, but do not remove these.
from . import _version
__version__ = _version.get_versions()['version']

from .app import app
