from django.conf.urls import url
from posts import views

urlpatterns = [

    
    url(r'^list/$', views.post_list, name="list"),
    url(r'^create/$', views.post_create, name="create"),
 	url(r'^update/(?P<slug>[-\w]+)/$', views.post_update, name="update"),
 	url(r'^delete/(?P<slug>[-\w]+)/$', views.post_delete, name="delete"),
 	url(r'^detail/(?P<slug>[-\w]+)/$', views.post_detail, name="detail"),


]