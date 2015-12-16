from django.conf.urls import url,patterns

urlpatterns = patterns('',
                       url(r'^test/$','data.views.test'),
                       )