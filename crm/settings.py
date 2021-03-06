import os
from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS as TCP
from datetime import timedelta
import sys

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# Override These
# =========================

# Make this unique, and don't share it with anybody.
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', '')

GOOGLE_API_KEY = os.environ.get('DJANGO_GOOGLE_API_KEY', '')

# A dictionary of Project IDs to arrays of User IDs that the
# project has permission to set the RFIDs of(None all IDs, [] no IDs)
USER_RFID_PROJECTS_TO_USERS = {}

# A dictionary of Project IDs to arrays of User IDs that the
# project has permission to change the balance of(None all IDs, [] no IDs)
USER_BALANCE_PROJECTS_TO_USERS = {}

# A dictionary of Project IDs to arrays of User IDs that the
# project has permission to send an email to(None all IDs, [] no IDs)
USER_EMAIL_PROJECTS_TO_USERS = {}

# Debug email backend
# uncomment to not use an SMTP service or actually send the email
# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# ==========================

GB_LIST = "roboclub-gb"
ACTIVE_LIST = "roboclub-members-18-19"

PROJECT_PRIVATE_KEY_MIN_LENGTH = 30

DEBUG = True
TEMPLATE_DEBUG = DEBUG

AUTH_PROFILE_MODULE = 'robocrm.RoboUser'

ADMINS = (
    ('Brent Strysko', 'bstrysko@andrew.cmu.edu'),
)

TEST_RUNNER = 'django.test.runner.DiscoverRunner'

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'crm',                      # Or path to database file if using sqlite3.
        'USER': 'root',                      # Not used with sqlite3.
        'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

GOOGLE_CALENDAR_ID = "85bf0h78fidsgkkgmkktrqasm8%40group.calendar.google.com"

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'America/New_York'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
# Set to False for simplicity and maintainability.
# Although storing datetimes and times in TZ Aware format is recommended,
# causes confusion to API and Admin end User.  Simplifies testing.
USE_TZ = False

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = os.path.join(BASE_DIR,'media')

PRIVATE_ROOT = os.path.join(BASE_DIR, 'private')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = '/media/'

PRIVATE_URL = '/private/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = os.path.join(BASE_DIR, 'static_root')

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    os.path.join(BASE_DIR,'static'),
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    ('pyjade.ext.django.Loader',(
        'django.template.loaders.filesystem.Loader',
        'django.template.loaders.app_directories.Loader',
    ),
    ),
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    #'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
    
    'crm.middleware.TemporaryRedirectFallbackMiddleware',
    
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'crm.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'crm.wsgi.application'

TEMPLATE_DIR = os.path.join(BASE_DIR, "templates")

TEMPLATE_DIRS = (
    TEMPLATE_DIR,
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.flatpages',
    'robocrm',
    'officers',
    'projects',
    'api',
    'webcams',
    'channels',
    'ordered_flatpages',
    'resources',
    'sponsors',
    'social_media',
    'links',
    'posters',
    'tshirts',
    'quotetron',
    'faq',
    'gallery',
    'announcements',
    'upcs',
    'push_server',
    'tinymce',
    'rest_framework',
    'ordered_model',
    'suit',
    'django.contrib.admin',
    'password_reset',
    'easy_thumbnails',
    'django_object_actions',
    'django.contrib.redirects',
    'rest_framework_swagger',
    'stock_items',

    # Uncomment the next line to enable admin documentation:
    # 'django.contrib.admindocs',
)

TINYMCE_DEFAULT_CONFIG = {
    'plugins': "table,spellchecker,paste,searchreplace",
    'theme': "advanced",
    'cleanup_on_startup': True,
    'custom_undo_redo_levels': 10,
    'theme_advanced_buttons3_add': 'code',
    'valid_elements': '*[*]',
    'convert_urls' : False,
    'relative_urls' : False,
    'forced_root_block' : False,
}

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.SessionAuthentication',
        'api.authentication.RCAuthentication',
    ),
    'DEFAULT_FILTER_BACKENDS': (
        'rest_framework.filters.DjangoFilterBackend',
    ),
    'DEFAULT_PARSER_CLASSES': (
        # allows Swagger to perform requests
        'rest_framework.parsers.MultiPartParser',
        'rest_framework.parsers.FormParser',

        # How everyone else should be making requests
        'rest_framework.parsers.JSONParser',
    ),
    'EXCEPTION_HANDLER': 'api.exception_handler.api_exception_handler',
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
        'rest_framework_csv.renderers.CSVRenderer',
    ),
    'DATETIME_FORMAT': '%m-%d-%YT%H:%M:%S',
}

SWAGGER_SETTINGS = {
    'api_version': '1.0',
    'is_authenticated': True,
    'permission_denied_handler': 'api.views.login_redirect_docs',
    'info': {
        'title': 'CMU Robotics Club API',
        'description': 'For further documentation & tutorials please visit '
                    '<a href="https://github.com/CMU-Robotics-Club/roboticsclub.org/wiki">the wiki</a>.',
    },
}

TEMPLATE_CONTEXT_PROCESSORS = TCP + (
    'django.core.context_processors.request',
)

THUMBNAIL_ALIASES = {
    '': {
        'poster_index': {
            # Aspect Ratio 1.6425855
            'size': (821, 500),
            'crop': True
        },
        'poster_admin': {
            # Aspect Ratio 1.6425855
            'size': (328, 200),
            'crop': True
        }
    },
}

SUIT_CONFIG = {
    'MENU_ICONS': {
        'announcements': 'icon-inbox',
        'api': 'icon-off',
        'auth': 'icon-user',
        'channels': 'icon-comment',
        'faq': 'icon-star',
        'gallery': 'icon-picture',
        'links': 'icon-globe',
        'officers': 'icon-th',
        'ordered_flatpages': 'icon-bookmark',
        'posters': 'icon-check',
        'projects': 'icon-random',
        'redirects': 'icon-refresh',
        'resources': 'icon-file',
        'robocrm': 'icon-tasks',
        'sites': 'icon-info-sign',
        'social_media': 'icon-thumbs-up',
        'sponsors': 'icon-gift',
        'stock_items': 'icon-list',
        'tshirts': 'icon-tag',
        'upcs': 'icon-list-alt',
        'webcams': 'icon-facetime-video',
    }
}

os.makedirs("{}/logs/".format(BASE_DIR), exist_ok=True)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'default': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
    },
    'handlers': {
        'django_file': {
            'level':'DEBUG',
            'class':'logging.handlers.RotatingFileHandler',
            'filename': '{}/logs/django_log.log'.format(BASE_DIR),
            'maxBytes': 1024*1024, # 1 MB
            'backupCount': 5,
            'formatter':'default',
        },
        'api_file': {
            'level':'DEBUG',
            'class':'logging.handlers.RotatingFileHandler',
            'filename': '{}/logs/api_log.log'.format(BASE_DIR),
            'maxBytes': 1024*1024, # 1 MB
            'backupCount': 5,
            'formatter':'default',
        },
        'apps_file': {
            'level':'DEBUG',
            'class':'logging.handlers.RotatingFileHandler',
            'filename': '{}/logs/apps_log.log'.format(BASE_DIR),
            'maxBytes': 1024*1024, # 1 MB
            'backupCount': 5,
            'formatter':'default',
        },   
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'default'
        },
    },
    'loggers': {
        'django': {
            'handlers': ['django_file', ],
            'level': 'DEBUG',
            'propagate': True,
        },
        'api': {
            'handlers': ['api_file', ],
            'level': 'DEBUG',
            'propagate': True,
        },
        'channels': {
            'handlers': ['apps_file', ],
            'level': 'DEBUG',
            'propagate': True,
        },
        'crm': {
            'handlers': ['apps_file', ],
            'level': 'DEBUG',
            'propagate': True,
        },
        'links': {
            'handlers': ['apps_file', ],
            'level': 'DEBUG',
            'propagate': True,
        },
        'officers': {
            'handlers': ['apps_file', ],
            'level': 'DEBUG',
            'propagate': True,
        },
        'ordered_flatpages': {
            'handlers': ['apps_file', ],
            'level': 'DEBUG',
            'propagate': True,
        },
        'projects': {
            'handlers': ['apps_file', ],
            'level': 'DEBUG',
            'propagate': True,
        },
        'resources': {
            'handlers': ['apps_file', ],
            'level': 'DEBUG',
            'propagate': True,
        },
        'robocrm': {
            'handlers': ['apps_file', ],
            'level': 'DEBUG',
            'propagate': True,
        },
        'social_media': {
            'handlers': ['apps_file', ],
            'level': 'DEBUG',
            'propagate': True,
        },
        'sponsors': {
            'handlers': ['apps_file', ],
            'level': 'DEBUG',
            'propagate': True,
        },
        'stock_items': {
            'handlers': ['apps_file', ],
            'level': 'DEBUG',
            'propagate': True,
        },
        'webcams': {
            'handlers': ['apps_file', ],
            'level': 'DEBUG',
            'propagate': True,
        },
    }
}

try:
    from .local_settings import *
except ImportError:
    pass

FONT_ROOT = os.path.join(STATIC_ROOT, "fonts")

# Only have BrowseableAPI in debug mode to help find errors
# Members should use Swagger for documentation
if DEBUG:
    REST_FRAMEWORK['DEFAULT_RENDERER_CLASSES'] += ('rest_framework.renderers.BrowsableAPIRenderer', )


# Monkey patch to fix error in 'ordered_model' app
from django.db.models.options import Options
@property
def monkeypatch__options__model_name(self):
    return self.model_name.lower()
Options.module_name = monkeypatch__options__model_name

