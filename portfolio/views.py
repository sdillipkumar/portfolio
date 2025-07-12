from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'index.html')


def about_me(request):
    return render(request, 'about_me.html')

def projects_view(request):
    return render(request, 'projects.html')