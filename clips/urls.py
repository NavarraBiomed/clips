from django.conf.urls import include, url
from django.contrib import admin


urlpatterns = [
    # Examples:
    # url(r'^$', 'clips.views.home', name='home'),

    url(r'^admin/', include(admin.site.urls)),
	url(r'^accounts/login/$', 'django.contrib.auth.views.login'),
    url(r'', include('studies_app.urls')),
]
