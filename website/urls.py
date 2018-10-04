from django.conf.urls import url
from website import views

urlpatterns = [
    url(r'^$', views.HomePageView.as_view()),
    url(r'^timeline$', views.TimelinePageView.as_view()),
    url(r'^about$', views.AboutPageView.as_view()),
    url(r'^contact$', views.ContactPageView.as_view()),
    url(r'^team$', views.TeamPageView.as_view()),
    url(r'^posts', views.PostsPageView.as_view()),
    url(r'^projects$', views.ProjectsPageView.as_view(), name='list-projects'),
    url(r'^markdown', views.ShowMD.as_view(), name='show-markdown'),
]
