from django.conf.urls import url
from . import views

urlpatterns = [url(r'^search/$',views.Search),
                       url(r'^home/$',views.Home),
                       url(r'SubmitFir',views.AddFir),
                       url(r'GetFir',views.GetFir),

                       ]
