EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
DEFAULT_FROM_EMAIL='registration@htcc2018.org'
SERVER_EMAIL = DEFAULT_FROM_EMAIL
EMAIL_HOST = 'smtp.webfaction.com'
EMAIL_HOST_USER = 'htcc2018'
EMAIL_HOST_PASSWORD = 'bol2018'

DEBUG = True
ALLOWED_HOSTS = ['htcc2018.org']

