from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views

app_name = 'accounts'

urlpatterns = [
    url(r'signup/$',views.SignUp.as_view(),name='signup'),
    url(r'profile/$',views.ProfileView.as_view(),name='profile'),
    url(r'detail/$',views.ProfileDetail.as_view(),name='detail'),
    url(r'login/$',auth_views.LoginView.as_view(template_name = 'accounts/login.html'),name='login'),
    url(r'logout/$',auth_views.LogoutView.as_view(),name='logout'),
    url(r'^update/(?P<pk>\d+)/$',views.UpdateProfile.as_view(),name='update'),
]
