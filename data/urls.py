from django.conf.urls import url,patterns

urlpatterns = patterns('',
                       url(r'^search/$','data.views.Search'),
                       url(r'^home/$','data.views.Home'),
                       url(r'SubmitFir','data.views.AddFir'),

                       )