from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from account_app.views import hello_world, AccountCreateView, AccountDetailView, AccountUpdateView

app_name = 'account_app'

urlpatterns = [
    path('create/', AccountCreateView.as_view(), name='create'),
    path('detail/<int:pk>', AccountDetailView.as_view(), name='detail'),
    path('update/<int:pk>', AccountUpdateView.as_view(), name='update'),

    path('login/', LoginView.as_view(template_name='account_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),

    path('hello_world', hello_world, name='hello_world'),
]
