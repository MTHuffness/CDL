from django.conf.urls import include, url
from django.contrib import admin
from draft.views import home, draft

admin.autodiscover()

urlpatterns = [
    # Examples:
    url(r'^$', home, name='home'),
    url(r'^draft$', draft, name='draft'),
    url(r'^admin/', include(admin.site.urls), name='admin'),
]
