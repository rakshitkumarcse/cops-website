from django.conf.urls import url
from howdy import views

urlpatterns = [
    url(r'^$', views.HomePageView.as_view()),
    url(r'^about$', views.AboutPageView.as_view()),
    url(r'^contact$', views.ContactPageView.as_view()),
    url(r'^blog$', views.BlogPageView.as_view()),
    url(r'^projects$', views.ProjectsPageView.as_view()),
]
