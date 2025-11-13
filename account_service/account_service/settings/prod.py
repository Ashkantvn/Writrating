from .base import *

SECURE_HSTS_SECONDS = 3600  # Tells browsers to always use HTTPS for site for 1 hour
SECURE_HSTS_INCLUDE_SUBDOMAINS = True  # Makes sure subdomains also use HTTPS
SECURE_HSTS_PRELOAD = True  # Lets site be added to browser lists that always use HTTPS

# SECURE_SSL_REDIRECT = True  # Automatically sends people to the HTTPS version of site

# SESSION_COOKIE_SECURE = True  # Keeps login cookies safe by only sending them over HTTPS

# CSRF_COOKIE_SECURE = True  # Keeps security tokens safe by only sending them over HTTPS

# Static files (CSS, JavaScript, Images)
STATIC_URL = "static/"
STATIC_ROOT = BASE_DIR / "staticfiles"