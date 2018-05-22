import markdown
from mdx_gfm import GithubFlavoredMarkdownExtension
from django.shortcuts import render
from django.views.generic import TemplateView
from csv import reader
from io import StringIO
from os import listdir


# Create your views here.
class HomePageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'index.html', context=None)


class AboutPageView(TemplateView):
    template_name = "about.html"


class PostsPageView(TemplateView):
    # Read the files in `posts` folder
    files = [f for f in listdir('posts')]

    # Post Tile Structure:
    # 0 : Post Title
    # 1 : Post Author
    # 2 : Time Posted
    # 3 : Tags
    # 4 : Image URL
    posts = []

    for filename in files:
        # Open the post.md file
        with open("posts/"+filename, "r") as f:
            content = f.read()

        i = content.find("---", 3)  # Get the ending ---, not the starting one
        content = content[4:i-2]       # Keep the header, remove everything else

        S = StringIO(content)
        mReader = reader(S, delimiter='=')
        temp = []

        for row in mReader:
            temp.append(row[1:2][0])

        # Add posting date too
        i = filename.find(":")
        temp.append(filename[:i])

        posts.append(temp)

    template_name = "posts.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['list_of_posts'] = self.posts
        return context


class ShowMD(TemplateView):
    template_name = 'markdown.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        with open('posts/README.md', 'r') as myfile:
            content = myfile.read()

        i = content.find("---", 3)  # Get the ending ---, not the starting one
        content = content[i:]  # Remove the header from content

        md = markdown.Markdown(extensions=[GithubFlavoredMarkdownExtension()])
        html = md.convert(content)

        context['markdown_content'] = html
        return context


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
