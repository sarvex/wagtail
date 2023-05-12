from django.conf import settings
from django.contrib.auth import views as auth_views
from django.urls import path, re_path

from wagtail import views
from wagtail.coreutils import WAGTAIL_APPEND_SLASH

serve_pattern = (
    r"^((?:[\w\-]+/)*)$" if WAGTAIL_APPEND_SLASH else r"^([\w\-/]*)$"
)
WAGTAIL_FRONTEND_LOGIN_TEMPLATE = getattr(
    settings, "WAGTAIL_FRONTEND_LOGIN_TEMPLATE", "wagtailcore/login.html"
)


urlpatterns = [
    path(
        "_util/authenticate_with_password/<int:page_view_restriction_id>/<int:page_id>/",
        views.authenticate_with_password,
        name="wagtailcore_authenticate_with_password",
    ),
    path(
        "_util/login/",
        auth_views.LoginView.as_view(template_name=WAGTAIL_FRONTEND_LOGIN_TEMPLATE),
        name="wagtailcore_login",
    ),
    # Front-end page views are handled through Wagtail's core.views.serve
    # mechanism
    re_path(serve_pattern, views.serve, name="wagtail_serve"),
]
