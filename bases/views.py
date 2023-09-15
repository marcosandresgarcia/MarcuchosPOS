from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views import generic


class UnauthorizedView(PermissionRequiredMixin):
    raise_exception = False
    redirect_field_name = "redirect_to"

    def handle_no_permission(self):
        self.login_url = "bases:unauthorized"
        return HttpResponseRedirect(reverse_lazy(self.login_url))


class Home(LoginRequiredMixin, generic.TemplateView):
    template_name = 'home/home.html'
    login_url = 'bases:login'


class HomeUnauthorizedView(generic.TemplateView):
    template_name = "bases/unauthorized.html"