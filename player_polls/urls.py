from django.conf.urls import url, include
from django.contrib import admin
from player_polls import views


app_name = 'player_polls'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^(?P<pk>[0-9]+)/players/(?P<slug>[0-9]+)/$', views.ResultsView.as_view(), name='results'),
    # Login UI
    url(r'^login/$', views.login_page_view, name="login_page"),
    # Login POST 
    url(r'^login/user_login/$', views.login_view, name="login_view"),
    # Logged In User Profile
    url(r'^user_profile/$', views.user_profile_view, name="user_profile_view"),
    # Logout POST
    url(r'^login/user_logout/$', views.logout_view, name="logout_view"),
    # Leave Comment
    url(r'^([0-9]+)/players/(?P<player_id>[0-9]+)/comment/$', views.comment_view, name="comment_view"),
    # Create Account View
    url(r'^create_account/$', views.create_account_view, name="create_account_view"),    
    # Create Account Post
    url(r'^create_user/$', views.create_user_post, name="create_user_post"),
]
