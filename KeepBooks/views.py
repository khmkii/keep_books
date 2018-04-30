from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm
from django.views import generic
from django.urls import reverse_lazy


class LandingPageView(generic.TemplateView):
    template_name = 'landing_page.html'


class LoginView(generic.FormView):
    form_class = AuthenticationForm
    success_url = reverse_lazy('accounts:home')
    template_name = "login.html"

    def form_valid(self, form):
        auth_login(self.request, form.get_user())
        return super().form_valid(form)


class LogoutView(generic.RedirectView):
    url = reverse_lazy('home')

    def get(self, request, *args, **kwargs):
        auth_logout(request)
        return super().get(request, *args, **kwargs)