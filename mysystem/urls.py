"""mysystem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include
from learn.views import *
from django.conf import settings


urlpatterns = [
    url(r'^$', index, name='homepage'),
    url(r'^login/', login),
    url(r'^crawlknowledge/', openCrawl),
    url(r'^uploadknowledge/', openUpload),
    url(r'^upload/', upload),
    url(r'^query/', openQuery),
    url(r'^queryprocess/', queryKnowledge),
    url(r'^crawl/', crawlKnowledge),
    url(r'^email/', sendemail),
    url(r'^sendemail/', email),
    url(r'^compareKnowledge/', openCompareKnowledge),
    url(r'^getContent/', getContent),
    url(r'^compareContent/', compareContent),
    url(r'^admin/', admin.site.urls),

]
if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns