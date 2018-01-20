from . import views
from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^d6275cf8e6b8\.html$', views.d6275cf8e6b8, name='d6275cf8e6b8'),

    url(r'^repetitor/$', views.repetitor, name='repetitor'),
    url(r'^vue/$', views.vue, name='vue'),# тестирование vue.js
    url(r'^less/$', views.less, name='less'),# тестирование vue.js
    url(r'^egemath/$', views.ege_math, name='ege_math'),
    url(r'^egetest/(?P<test_id>[0-9]+)/$', views.egetest, name='egetest'),
    url(r'^administrator/$', views.administrator, name='administrator'),
    url(r'^ege_test_input/(?P<test_num>[0-9]+)/(?P<task_num>[0-9]+)/$', views.ege_test_input, name='ege_test_input'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^logout/$', views.logout_view, name='logout_view'),
    url(r'^login/$', views.log, name='log'),
    url(r'^repetitor_math/thanks/$', views.thanks, name='thanks'),
    url(r'^egetaskanswer/$', views.egetaskanswer, name='egetaskanswer'),
    url(r'^egetask/$', views.egetask, name='egetask'),
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
