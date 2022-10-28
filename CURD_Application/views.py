from django.shortcuts import render
from django.shortcuts import redirect
from django.template import loader
from .models import Show
from django.urls  import reverse
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.
def show(request):
    first = request.POST.get('name')
    middle = request.POST.get('number')
    last = request.POST.get('Email')
    value = Show(name = first, number = middle, Email = last)
    if request.method == 'POST':
        value.save()
        print(first)
        return redirect('show')
    
    hello = Show.objects.all()
    return render(request, 'index.html',{'hello':hello})

def update(request,id):
    kal = Show.objects.get(id = id)
    first, middle, last = kal.name, kal.number, kal.Email
    value = {
        'first':first,
        'middle': middle,
        'last' : last
    }
    if request.method == 'POST':
        kal.name = request.POST.get('name')
        kal.number = request.POST.get('number')
        kal.Email = request.POST.get('Email')
        kal.save()
        return redirect('show')

    return render(request, 'udpate.html', (value))

def delete(request,id):
    kal = Show.objects.get(id = id)
    kal.delete()
    print(kal)
    #return HttpResponseRedirect(reverse('show'))
    return redirect('show')




