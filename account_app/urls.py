from django.urls import path

from account_app.views import hello_world

app_name = 'account_app'

urlpatterns = [
    path('hello_world', hello_world, name='hello_world')
]