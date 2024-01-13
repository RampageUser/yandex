from django.contrib.auth.views import (
    LoginView,
    LogoutView,
    PasswordChangeView,
    PasswordChangeDoneView,
    PasswordResetView,
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView
)
from django.contrib.auth import login
from django.http import Http404
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import UpdateView
from .forms import RegistrationForm, ProfileForm
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
    context = {'form': form}
    return render(request, 'users/signup.html', context)


class CustomLoginView(LoginView):
    template_name = 'users/login.html'


class CustomLogoutView(LogoutView):
    template_name = 'users/logged_out.html'


class CustomPasswordChangeView(PasswordChangeView):
    template_name = 'users/password_change_form.html'
    success_url = reverse_lazy('users:password_change_done')


class CustomPasswordChangeDoneView(PasswordChangeDoneView):
    template_name = 'users/password_change_done.html'


class CustomPasswordResetView(PasswordResetView):
    template_name = 'users/password_reset_form.html'
    email_template_name = 'users/password_reset_email.html'
    success_url = reverse_lazy('users:password_reset_done')


class CustomPasswordResetDoneView(PasswordResetDoneView):
    template_name = 'users/password_reset_done.html'


class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = 'users/password_reset_confirm.html'
    success_url = reverse_lazy('users:password_reset_complete')


class CustomPasswordResetCompleteView(PasswordResetCompleteView):
    template_name = 'users/password_reset_complete.html'


class ProfileView(UpdateView):
    template_name = 'users/profile.html'
    form_class = ProfileForm
    success_url = reverse_lazy('posts:index')
    pk_url_kwarg = 'id'

    def get_queryset(self):
        user_id = self.kwargs.get('id')
        queriset = CustomUser.objects.filter(pk=user_id)
        if not queriset.exists():
            raise Http404('User does not exist')
        return queriset
