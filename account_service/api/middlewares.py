from django.http import HttpResponseForbidden

class BlockBotMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response  # Store the next middleware or view

    def __call__(self, request):
        # Extract the User-Agent header from the request
        user_agent = request.META.get('HTTP_USER_AGENT', '')

        # List of known bad bots or patterns (can be expanded)
        blocked_agents = ['BadBot', 'curl', 'wget', 'python-requests']

        # Check if any blocked agent is in the User-Agent string
        if any(bot in user_agent.lower() for bot in blocked_agents):
            return HttpResponseForbidden("Access denied: bot detected")

        # Continue processing the request if no bot is detected
        response = self.get_response(request)
        return response