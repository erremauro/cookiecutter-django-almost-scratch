"""
Django local settings for errews project.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/
"""

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'h4iko*4-so7d3ai5ry1mb_9t^v4=s!kc=$&5@u)ea=0q^fuoym'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': '{{cookiecutter.pgsql_local_database}}',
        'USER': '{{cookiecutter.pgsql_local_username}}',
        'PASSWORD': '{{cookiecutter.pgsql_local_password}}',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}