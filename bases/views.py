from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views import generic


class UnauthorizedView(LoginRequiredMixin, PermissionRequiredMixin):
    raise_exception = False
    redirect_field_name = "redirect_to"
    login_url = "bases:login"

    def handle_no_permission(self):
        from django.contrib.auth.models import AnonymousUser
        if not self.request.user==AnonymousUser():
            self.login_url = "bases:unauthorized"
        return HttpResponseRedirect(reverse_lazy(self.login_url))


class Home(LoginRequiredMixin, generic.TemplateView):
    template_name = 'home/home.html'
    login_url = 'bases:login'


class HomeUnauthorizedView(LoginRequiredMixin, generic.TemplateView):
    login_url = "bases:login"
    template_name = "bases/unauthorized.html"


class BaseCreateView(SuccessMessageMixin, UnauthorizedView, generic.CreateView):
    context_object_name = 'obj'
    success_message = "Registro Creado Satisfactoriamente"

    def form_valid(self, form):
        form.instance.creation_user = self.request.user
        return super().form_valid(form)


class BaseUpdateView(SuccessMessageMixin, UnauthorizedView, generic.UpdateView):
    context_object_name = 'obj'
    success_message = "Registro Actualizado Satisfactoriamente"

    def form_valid(self, form):
        form.instance.update_user = self.request.user
        return super().form_valid(form)


class BaseDeleteView(SuccessMessageMixin, UnauthorizedView, generic.DeleteView):
    context_object_name = 'obj'
    success_message = "Registro Eliminado Satisfactoriamente"

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        return HttpResponseRedirect(self.get_success_url())