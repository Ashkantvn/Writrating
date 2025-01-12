from core.permissions import IsSuperUser
from rest_framework.authentication import SessionAuthentication
from drf_yasg import openapi
from drf_yasg.views import get_schema_view


class CsrfExemptSessionAuthentication(SessionAuthentication):
    def enforce_csrf(self, request):
        return


schema_view = get_schema_view(
    openapi.Info(
        title="Writrating API",
        default_version="v1",
        description="API documentation",
        terms_of_service="https://www.google.com/policies/terms/",
        license=openapi.License(name="BSD License"),
    ),
    public=False,
    permission_classes=(IsSuperUser,),
    authentication_classes=[CsrfExemptSessionAuthentication],
)
