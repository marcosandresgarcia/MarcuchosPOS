from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import generic

from inv.forms import CategoryForm
from inv.models import Category


class Categoryview(LoginRequiredMixin, generic.ListView):
    model = Category
    template_name = "inv/category.html"
    context_object_name = "obj"
    login_url = "bases:login"


class CategoryCreate(LoginRequiredMixin, generic.CreateView):
    model = Category
    template_name = "inv/category_form.html"
    context_object_name = "obj"
    form_class = CategoryForm
    success_url = reverse_lazy("inv:category")
    login_url = "bases:login"

    def form_valid(self, form):
        form.instance.creation_user = self.request.user
        return super().form_valid(form)


class CategoryUpdate(LoginRequiredMixin, generic.UpdateView):
    model = Category
    template_name = "inv/category_form.html"
    context_object_name = "obj"
    form_class = CategoryForm
    success_url = reverse_lazy("inv:category")
    login_url = "bases:login"

    def form_valid(self, form):
        form.instance.update_user = self.request.user
        return super().form_valid(form)