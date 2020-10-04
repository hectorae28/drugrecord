from users.forms import SignUpForm
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.views.generic import FormView,DetailView,ListView
from django.contrib.auth import views as auth_views
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.
class SignUpView(FormView):
    template_name='user/signup.html'
    form_class=SignUpForm
    success_url = reverse_lazy('users:login')

    def form_valid(self,form):
        form.save()
        return super().form_valid(form)


class UserDetailsView(LoginRequiredMixin,DetailView):
    template_name = ".html"
    slug_field='username'
    slug_url_kwarg='username'
    queryset=User.objects.all()
    context_object_name='user'

class DashboardView(LoginRequiredMixin,ListView):
    template_name='user/dashboard.html'
    model=User
    context_object_name='user'


class LoginView(auth_views.LoginView):
    template_name='user/login.html'

class LogoutView(LoginRequiredMixin,auth_views.LogoutView):
    template_name='user/logged_out.html'

