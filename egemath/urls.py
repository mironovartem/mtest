from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    #url(r'^$', views.home_page, name='home_page'),
    #url(r'^home/$', views.home_page, name='home_page'),
    #url(r'^accounts/profile/$', views.home_page, name='home_page'),
    url(r'^$', views.ege_math, name='ege_math'),
    url(r'^egemath/$', views.ege_math, name='ege_math'),
    url(r'^egetest/(?P<test_id>[0-9]+)/$', views.egetest, name='egetest'),
    url(r'^about/$', views.about, name='about'),
    url(r'^about_me/$', views.about_me, name='about_me'),
    url(r'^repetitor_math/$', views.repetitor_math, name='repetitor_math'),
    url(r'^donate/$', views.donate, name='donate'),
    url(r'^copyright/$', views.copyright, name='copyright'),
    url(r'^advertising/$', views.advertising, name='advertising'),
    url(r'^website_development/$', views.website_development, name='website_development'),
    url(r'^contacts/$', views.contacts, name='contacts'),
    #url(r'^egetest/(?P<test_id>[0-9]+)/egetestanswer$', views.egetestanswer, name='egetestanswer'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^subscribe/$', views.subscribe, name='subscribe'),
    url(r'^todo/$', views.todo, name='todo'),
    url(r'^logout/$', views.logout_view, name='logout_view'),
    url(r'^login/$', views.log, name='log'),
    url(r'^repetitor_math/thanks/$', views.thanks, name='thanks'),
    url(r'^egetaskanswer/$', views.egetaskanswer, name='egetaskanswer'),
    url(r'^egetask/$', views.egetask, name='egetask'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
