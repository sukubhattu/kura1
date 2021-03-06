from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views as auth_views

from accounts import views as accounts_views
from boards import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    url(r'^postman/', include('postman.urls')),
    url(r'^articles/', include('articles.urls')),
    url(r'^$', views.BoardListView.as_view(), name='home'),
    url(r'^signup/$', accounts_views.signup, name='signup'),
    url(r'^login/$', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    url(r'^logout/$', auth_views.LogoutView.as_view(), name='logout'),

    url(r'^reset/$',
        auth_views.PasswordResetView.as_view(
            template_name='password_reset.html',
            email_template_name='password_reset_email.html',
            subject_template_name='password_reset_subject.txt'
        ),
        name='password_reset'),
    url(r'^reset/done/$',
        auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'),
        name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'),
        name='password_reset_confirm'),
    url(r'^reset/complete/$',
        auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'),
        name='password_reset_complete'),

    url(r'^settings/account/$', accounts_views.UserUpdateView.as_view(), name='my_account'),
    url(r'^profile/(?P<user_id>\d+)/(?P<value>\d+)/$', accounts_views.ProfileView, name='profile'),
    url(r'^settings/password/$', auth_views.PasswordChangeView.as_view(template_name='password_change.html'),
        name='password_change'),
    url(r'^settings/password/done/$', auth_views.PasswordChangeDoneView.as_view(template_name='password_change_done.html'),
        name='password_change_done'),

    url(r'^boards/(?P<pk>\d+)/$', views.TopicListView.as_view(), name='board_topics'),
    url(r'^boards/(?P<pk>\d+)/new/$', views.new_topic, name='new_topic'),
    url(r'^boards/(?P<pk>\d+)/topics/(?P<topic_pk>\d+)/$', views.PostListView.as_view(), name='topic_posts'),
    url(r'^boards/(?P<pk>\d+)/topics/(?P<topic_pk>\d+)/reply/$', views.reply_topic, name='reply_topic'),
    url(r'^boards/(?P<pk>\d+)/topics/(?P<topic_pk>\d+)/posts/(?P<post_pk>\d+)/edit/$',
        views.PostUpdateView.as_view(), name='edit_post'),
    url(r'^admin/', admin.site.urls),
    url(r'^boards/posts/(?P<post_id>\d+)/upvote', views.PostUpvote, name='upvote_post'),
    url(r'^boards/posts/(?P<post_id>\d+)/downvote', views.PostDownvote, name='downvote_post'),
    url(r'^boards/topic/(?P<topic_id>\d+)/upvote', views.TopicUpvote, name='upvote_topic'),
    url(r'^boards/topic/(?P<topic_id>\d+)/downvote', views.TopicDownvote, name='downvote_topic'),
    url(r'^boards/topic/(?P<post_pk>\d+)', views.DeletePost, name='delete_posts'),
    url(r'^boards/(?P<board_id>\d+)/search/$', views.SearchTopic, name='search_topics'),
    url(r'^contact_us/$', views.ContactUs, name='contact'),
    url(r'^contact_us/feedback$', views.Feedback, name='feedback'),
]
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
