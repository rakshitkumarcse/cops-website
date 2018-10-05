import markdown
from mdx_gfm import GithubFlavoredMarkdownExtension
from django.shortcuts import render
from django.views.generic import TemplateView
from csv import reader
from io import StringIO
from os import listdir


class HomePageView(TemplateView):
    template_name = "index.html"


class TeamPageView(TemplateView):
    '''
    TODO Add integrate this into team page

    # Read the csv file coordinators.csv
    with open("website/coordinators.csv", "r") as f:
        r = reader(f)
        rest = [row for row in r]
        rest = rest[1:]  # Remove the top row: Name, Email, etc

    template_name = "team.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['objects'] = self.rest
        return context
    '''
    template_name = "team.html"


class TimelinePageView(TemplateView):
    template_name = "timeline.html"


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
        mReader = reader(S, delimiter='\n')
        temp = []

        for row in mReader:
            k = row[0].find('=')    # Find index of `=`
            temp.append(row[0][k+1:])

        # Change posts tag to a list
        temp[2] = temp[2].split(',')

        # Add posting date too
        i = filename.find(":")
        temp.append(filename[:i])

        # Add filename to temp. For later
        temp.append(filename)

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

        with open(self.request.GET.get('id'), 'r') as myfile:
            content = myfile.read()

        i = content.find("---", 3)  # Get the ending ---, not the starting one
        content = content[i+3:]  # Remove the header from content

        md = markdown.Markdown(extensions=[GithubFlavoredMarkdownExtension()])
        html = md.convert(content)

        context['markdown_content'] = html
        return context


class ProjectsPageView(TemplateView):
    # Read the files in `projects` folder
    files = [f for f in listdir('projects')]

    # Project Tile Structure:
    # 0 : Project Title
    # 1 : Description
    # 2 : Tags
    # 3 : Image URL
    projects = []

    for filename in files:
        # Open the post.md file
        with open("projects/" + filename, "r") as f:
            content = f.read()

        i = content.find("---", 3)  # Get the ending ---, not the starting one
        content = content[4:i - 2]  # Keep the header, remove everything else

        S = StringIO(content)
        mReader = reader(S, delimiter='\n')
        temp = []

        # Add filename to temp. For later use. Remove the last `.md`
        k = filename.find('.md')
        temp.append(filename[:k])

        for row in mReader:
            k = row[0].find('=')  # Find index of `=`
            temp.append(row[0][k + 1:])

        # Change projects tag to a list
        temp[2] = temp[2].split(',')

        projects.append(temp)

    template_name = "projects.htm"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['list_of_projects'] = self.projects
        return context
