from django.conf.urls import include, url
from django.contrib import admin
from material.frontend import urls as frontend_urls

urlpatterns = [
    # Examples:
    # url(r'^$', 'clips.views.home', name='home'),
    
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('clips_app.urls')),
    #url(r'', include(frontend_urls)),
]