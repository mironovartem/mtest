from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', views.home_page, name='home_page'),
    #url(r'^home/$', views.home_page, name='home_page'),
    #url(r'^accounts/profile/$', views.home_page, name='home_page'),
    url(r'^egemath/$', views.ege_math, name='ege_math'),
    url(r'^egetest/(?P<test_id>[0-9]+)/$', views.egetest, name='egetest'),
    url(r'^egetest/(?P<test_id>[0-9]+)/egetestanswer$', views.egetestanswer, name='egetestanswer'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^logout/$', views.logout_view, name='logout_view'),
    url(r'^login/$', views.log, name='log'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)