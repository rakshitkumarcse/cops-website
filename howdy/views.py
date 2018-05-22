from django.shortcuts import render
from django.views.generic import TemplateView
from csv import reader


# Create your views here.
class HomePageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'index.html', context=None)


class AboutPageView(TemplateView):
    template_name = "about.html"


class BlogPageView(TemplateView):
    template_name = "blog.html"


class ContactPageView(TemplateView):
    # Read the csv file coordinators.csv
    with open("howdy/coordinators.csv", "r") as f:
        r = reader(f)
        rest = [row for row in r]
        rest = rest[1:]  # Remove the top row: Name, Email, etc

    template_name = "contact.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['objects'] = self.rest
        return context


class ProjectsPageView(TemplateView):
    template_name = "projects.html"
