from typing import Any
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import login
from django.db.models.query import QuerySet
from django.http import Http404
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import UpdateView
from .forms import RegistrationForm, ProfilForm
from .models import CustomUser


def sign_up(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user=user)
            return redirect('posts:index')
    else:
        form = RegistrationForm()
    context = {
        'form': form
    }
    return render(request, 'users/signup.html', context)



class CustomLoginView(LoginView):
    template_name = 'users/login.html'


class CustomLogoutView(LogoutView):
    template_name = 'users/logged_out.html'


class ProfilView(UpdateView):
    template_name = 'users/profil.html'
    form_class = ProfilForm
    success_url = reverse_lazy('posts:index' )
    pk_url_kwarg = 'id'

    def get_queryset(self) -> QuerySet[Any]:
        user_id = self.kwargs.get('id')
        queriset = CustomUser.objects.filter(pk=user_id)
        if not queriset.exists():
            raise Http404('User does not exist')
        return queriset
        