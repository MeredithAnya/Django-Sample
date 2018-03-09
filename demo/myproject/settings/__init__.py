# This implements a common pattern of having a base settings file
# and additional settings files for each environment where the django
# application will run; the appropriate one is usually chosen with
# a command line option, environment variable, or flag file on disk.
#
# In this case, editing the USE_DEV_SETTINGS value will allow switching
# between "development" and "production" values.

from __future__ import absolute_import

from .base import *


USE_DEV_SETTINGS = True
# Note that setting this to False will load "production-like" settings
# that include disabling Debug mode (error details will be hidden) and
# not serving static files from the "runserver" command (the CSS and
# Favicon files won't work)

if USE_DEV_SETTINGS:
    from .development import *
    ENV = 'development'
else:
    from .production import *
    ENV = 'production'

import os
import raven
# After the other settings are loaded, build the config dict that Raven will use

RAVEN_CONFIG = {
    'dsn': MY_SENTRY_DSN,
    'environment': ENV,
    'release': raven.fetch_git_sha(os.path.abspath(os.path.dirname('..'))),   # You can track different releases of your app in Sentry
                          # See https://docs.sentry.io/learn/releases/ for details
}
