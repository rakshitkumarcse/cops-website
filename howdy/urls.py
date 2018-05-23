from django.conf.urls import url
from howdy import views

urlpatterns = [
    url(r'^$', views.AboutPageView.as_view()),
    url(r'^about$', views.AboutPageView.as_view()),
    url(r'^contact$', views.ContactPageView.as_view()),
    url(r'^posts', views.PostsPageView.as_view()),
    url(r'^projects$', views.ProjectsPageView.as_view()),
    url(r'^markdown', views.ShowMD.as_view()),
]
