import os

# Flask config
DEBUG=False
IP=os.environ.get('APP_IP', '0.0.0.0')
PORT=os.environ.get('APP_PORT', '8080')
SERVER_NAME = os.environ.get('APP_SERVER_NAME', 'superduperpancake.csh.rit.edu')
SECRET_KEY = os.environ.get('APP_SECRET_KEY', 'thisisntverysecure')

# OpenID Connect SSO config
OIDC_ISSUER = os.environ.get('APP_OIDC_ISSUER', '')
OIDC_CLIENT_CONFIG = {
    'client_id': os.environ.get('APP_OIDC_CLIENT_ID', 'superduperpancake'),
    'client_secret': os.environ.get('APP_OIDC_CLIENT_SECRET', ''),
    'post_logout_redirect_uris': [os.environ.get('APP_OIDC_LOGOUT_REDIRECT_URI',
        'https://superduperpancake.csh.rit.edu/logout')]
}
