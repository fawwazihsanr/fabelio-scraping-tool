"""djangoProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, re_path
from django.shortcuts import render
from django.conf.urls import url
from django.views import static
from django.conf import settings

from . import views


def render_react(request):
    return render(request, "index.html")


urlpatterns = [
    path('admin/', admin.site.urls),
    path('submission', views.create_submission, name='submission'),
    path('submission/list', views.get_submission, name='get_submission'),
    path('submission/<int:id>', views.get_submission_by_id, name='get_submission_by_id'),
    url(r'^static/(?P<path>.*)$', static.serve,
        {'document_root': settings.STATIC_ROOT}, name='static'),
    re_path(r"^$", render_react),
    re_path(r"^(?:.*)/?$", render_react),
]
