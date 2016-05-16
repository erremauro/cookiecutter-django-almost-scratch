import os

"""
Import local configuration if DJANGO_ENV environment
variable is set to DEV, otherwise load production configurations.
"""

from .common import *

if ('dev' == os.environ['DJANGO_ENV']):
	from .local import *
else:
	from .production import *
