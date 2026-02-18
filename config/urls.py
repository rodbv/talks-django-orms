"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from django.views.generic import RedirectView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("__reload__/", include("django_browser_reload.urls")),
    path("", RedirectView.as_view(url="/vendas/")),
    path("", include("casas_floripa.urls")),
]

if settings.DEBUG:
    extra = []
    if getattr(settings, "USE_SILK", False):
        extra.append(path("silk/", include("silk.urls", namespace="silk")))
    if getattr(settings, "USE_DDT", False):
        extra.append(path("__debug__/", include("debug_toolbar.urls")))
    urlpatterns = extra + urlpatterns
