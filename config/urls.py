# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin

urlpatterns = [
    # Django Admin
    url(r'^admin/', include(admin.site.urls)),

    # Puput
    url(r'', include('puput.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
