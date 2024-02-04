from django.shortcuts import render, redirect

from main.models import About, Specialized, Categoriya, Portfolio, Experience, Team, News, Post


def index(request):
    contex = {
        'about': About.objects.all().order_by('-id')[0:1],
        'specialized': Specialized.objects.all(),
        'categoriya': Categoriya.objects.all(),
        'portfolio': Portfolio.objects.all(),
        'experience': Experience.objects.all(),
        'team': Team.objects.all(),
        'news': News.objects.all(),
        "post": Post.objects.all()
    }
    return render(request, 'main/index.html', contex)

def portfolio(request, id):
    context = {
        'portfolio': Portfolio.objects.filter(categoriya_id=id)
    }
    return render(request, 'main/index.html', context)


def post(request):
    if request.method == 'POST':
        a = Post(name=request.POST['name'], email=request.POST['email'], subject=request.POST['subject'], text=request.POST['text'], title=request.POST['title'])
        print(a, "okkk")
        a.save()
        return redirect("index")
    return render(request, 'main/index.html')

