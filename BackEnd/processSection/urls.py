from . import views
from django.urls import path
from django.conf.urls import url
urlpatterns=[
    url(r'^$',views.process),
    # url(r'^$',views.testwhere),
]