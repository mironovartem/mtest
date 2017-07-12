from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home_page, name='home_page'),
    url(r'^home/$', views.home_page, name='home_page'),
    #url(r'^accounts/profile/$', views.profile, name='profile'),
    url(r'^egemath/$', views.ege_math, name='ege_math'),
    url(r'^egetest/(?P<test_id>[0-9]+)/$', views.egetest, name='egetest'),
    url(r'^egetest/(?P<test_id>[0-9]+)/egetestanswer$', views.egetestanswer, name='egetestanswer'),
    url(r'^signup/$', views.signup, name='signup'),
    #url(r'^login\.html$', views.login, name='login'),

]
