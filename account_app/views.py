from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from account_app.models import HelloWorld


# Create your views here.

def hello_world(request):
  if request.method == 'POST':
    text = request.POST.get('hello_world_input')

    model = HelloWorld()
    model.text = text
    model.save()

    models = HelloWorld.objects.all()

    return HttpResponseRedirect(reverse('account_app:hello_world'))

  elif request.method == 'GET':
    models = HelloWorld.objects.all()
    return render(request,
                  'account_app/hello_world.html',
                  context={
                    'outputs': models
                  })