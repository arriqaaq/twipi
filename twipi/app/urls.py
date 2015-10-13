from django.conf.urls import include, url
from app import views

urlpatterns = [
	url(r'^$', views.test, name='test'),    
	url(r'^login/$', views.user_login, name='login'),
	url(r'^submit/$', views.submit, name='submit'),
	url(r'^user/(?P<user_id>[\w\-]+)/$', views.viewUser, name='viewTweet'),        
	url(r'^retweet/(?P<tweet_id>[\w\-]+)/$', views.retweet, name='retweet'),
        url(r'^replies/(?P<tweet_id>[\w\-]+)/$', views.replies, name='replies'),
	url(r'^reply/(?P<tweet_id>[\w\-]+)/$', views.viewTweet, name='viewTweet'),   
	url(r'^follow/(?P<user_id>[\w\-]+)/$', views.follow, name='follow'),   
	url(r'^logout/$', views.user_logout, name='logout'),   

]
