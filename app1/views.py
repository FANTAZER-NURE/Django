from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


# def index(request):
#     return render(request, 'app1/home.html')


def main(request):
    # return HttpResponse("<h1>aboba2</h1>")
    return render(request, 'app1/index.html')


def contacts(request, color="#c19b76"):
    phone = request.GET.get('phone', 3801234567)
    mail = request.GET.get('mail', 'mail@gmail.com')
    phoneandmail = {
        'phone': phone,
        'mail': mail,
        'color': color
    }
    return render(request, 'app1/contact.html', phoneandmail)


def rooms(request):
    return render(request, 'app1/room.html')

# def color(request, color = "black"):





