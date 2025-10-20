from drf_spectacular.extensions import OpenApiAuthenticationExtension

class StatelessJWTAuthenticationScheme(OpenApiAuthenticationExtension):
    target_class = 'devices_service.authentication.StatelessJWTAuthentication'
    name = 'StatelessJWTAuth'

    def get_security_definition(self, auto_schema):
        return {
            'type': 'http',
            'scheme': 'bearer',
            'bearerFormat': 'JWT',
        }