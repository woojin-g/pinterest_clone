from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from account_app.forms import AccountUpdateForm
from account_app.models import HelloWorld


class AccountCreateView(CreateView):
  model = User
  form_class = UserCreationForm
  success_url = reverse_lazy('account_app:login')
  template_name = 'account_app/create.html'


class AccountDetailView(DetailView):
  model = User
  context_object_name = 'target_user'
  template_name = 'account_app/detail.html'


class AccountUpdateView(UpdateView):
  model = User
  form_class = AccountUpdateForm
  success_url = reverse_lazy('account_app:hello_world')
  template_name = 'account_app/update.html'


class AccountDeleteView(DeleteView):
  model = User
  success_url = reverse_lazy('account_app:login')
  template_name = 'account_app/delete.html'


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