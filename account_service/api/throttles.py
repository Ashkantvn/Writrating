from rest_framework.throttling import SimpleRateThrottle


class BurstRateThrottle(SimpleRateThrottle):
    # This links to the 'burst' rate defined in settings.py
    scope = "burst"

    def get_cache_key(self, request, view):
        if not request.user.is_authenticated:
            # Use IP address to identify the client
            return self.get_ident(request)

        # If the user is logged in (authenticated)
        # Use the username to identify the client
        return request.user.username
