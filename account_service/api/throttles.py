from rest_framework.throttling import SimpleRateThrottle 

class BurstRateThrottle(SimpleRateThrottle):
    scope = 'burst'  # This links to the 'burst' rate defined in settings.py

    def get_cache_key(self, request, view):
        if not request.user.is_authenticated:
            return self.get_ident(request)  # Use IP address to identify the client

        # If the user is logged in (authenticated)
        return request.user.username  # Use the username to identify the client