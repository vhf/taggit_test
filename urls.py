# -*- coding: utf-8 -*-:
from django.conf.urls import patterns, url

from bug.views import root

urlpatterns = patterns(
    '',

    url(r'^$', root, name="root"),

)
