from django.shortcuts import render
from .models import Users


# Create your views here.
def index(request):
    return render(request, 'index.html')


def contact(request):
    return render(request, 'contact.html')


def trainer(request):
    return render(request, 'trainer.html')


def why(request):
    return render(request, 'why.html')


def blog(request):
    return render(request, 'blog.html')


def login(request):
    return render(request, 'login.html')


def register(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')

        # create an object
        new_person = Users(first_name=first_name, last_name=last_name, email=email, password=password)
        new_person.save()

        # get all persons-displays everything in the database.
    people = Users.objects.all()
    return render(request, 'register.html', context={'people': people})
