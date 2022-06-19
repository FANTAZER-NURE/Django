from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import CustomerForm
from .models import Customer, Room



# def index(request):
#     return render(request, 'app1/home.html')



def main(request):
    # return HttpResponse("<h1>aboba2</h1>")
    return render(request, 'app1/index.html')

@login_required(login_url='/accounts/login/')
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


def list(request):
    customers = Customer.objects.all()
    rooms = Room.objects.all();
    return render(request, 'app1/list.html', {'customers': customers, 'rooms': rooms})


def book(request):
    form = CustomerForm()
    error = ''

    if request.method == 'GET':
        return render(request, 'app1/book.html')

    if request.method == 'POST':
        form = CustomerForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('list')
        else:
            error: 'Incorrect'

    data = {
        'form': form
    }

    return render(request, 'app1/book.html', data)




