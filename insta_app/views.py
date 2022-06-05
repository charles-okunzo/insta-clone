from django.shortcuts import render

# Create your views here.


def home(request):
    context={}
    return render(request,'insta_app/index.html', context)

def posts(request):
    title  = 'Instagram | All posts'
    context = {'title':title}
    return render(request, 'insta_app/posts.html', context)