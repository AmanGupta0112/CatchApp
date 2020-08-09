from django.conf.urls import url
from . import views

app_name = 'RetryApp'

urlpatterns = [
    url(r'contactus/$',views.ContactUsView.as_view(),name='contactus'),
    url(r'feedback/$',views.FeedbackView.as_view(),name='feedback'),
    url(r'newapp/$',views.NewApp.as_view(),name='newapp'),
    url(r'newsoft/$',views.NewSoft.as_view(),name='newsoft'),
    url(r'newweb/$',views.NewWeb.as_view(),name='newweb'),
    url(r'searched/$',views.searchview,name='searched'),
]
