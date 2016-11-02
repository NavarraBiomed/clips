from django.conf import settings
from django.conf.urls import include, url
from django.views.generic.base import RedirectView
from . import views

urlpatterns = [
    url(r'^$', views.study_list),
    url (r'^study/(?P<study_id>[0-9]+)/$', views.study_details),
    url (r'^study/(?P<study_pk>[0-9]+)/case/(?P<case_pk>[0-9]+)/edit/$', views.case_edit, name ='case_edit'),
    url (r'^study/(?P<study_id>[0-9]+)/new/$', views.new_case),
    url (r'^study/(?P<study_id>[0-9]+)/validate/$', views.validate_case),
    url (r'^study/(?P<study_id>[0-9]+)/json/$', views.study_json),
    url (r'^study/(?P<study_id>[0-9]+)/info/$', views.study_info),
    url (r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}),

]
