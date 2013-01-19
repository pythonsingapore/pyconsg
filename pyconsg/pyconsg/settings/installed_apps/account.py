"""Settings for the ``account`` app."""
ACCOUNT_OPEN_SIGNUP = True
ACCOUNT_USE_OPENID = False
ACCOUNT_REQUIRED_EMAIL = False
ACCOUNT_EMAIL_VERIFICATION = False
ACCOUNT_EMAIL_AUTHENTICATION = False
ACCOUNT_UNIQUE_EMAIL = EMAIL_CONFIRMATION_UNIQUE_EMAIL = False

ACCOUNT_SIGNUP_REDIRECT_URL = 'dashboard'
ACCOUNT_LOGIN_REDIRECT_URL = 'dashboard'
ACCOUNT_LOGOUT_REDIRECT_URL = 'home'
ACCOUNT_USER_DISPLAY = lambda user: user.email

AUTHENTICATION_BACKENDS = [
    # Permissions Backends
    'symposion.teams.backends.TeamPermissionsBackend',

    # Auth backends
    'account.auth_backends.EmailAuthenticationBackend',
]

LOGIN_URL = "/account/login/"

EMAIL_CONFIRMATION_DAYS = 2
