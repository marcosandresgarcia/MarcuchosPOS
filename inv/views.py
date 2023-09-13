from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views import generic

from inv.forms import CategoryForm, ProductForm
from inv.models import Category, Product


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


class CategoryDelete(LoginRequiredMixin, generic.DeleteView):
    model = Category
    template_name = "inv/category_delete.html"
    context_object_name = "obj"
    success_url = reverse_lazy("inv:category")


class ProductView(LoginRequiredMixin, generic.ListView):
    model = Product
    template_name = "inv/products.html"
    context_object_name = "obj"
    login_url = "bases:login"


class ProductCreate(LoginRequiredMixin, generic.CreateView):
    model = Product
    template_name = "inv/products_form.html"
    context_object_name = "obj"
    form_class = ProductForm
    success_url = reverse_lazy("inv:product")
    login_url = "bases:login"

    def form_valid(self, form):
        form.instance.creation_user = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(ProductCreate, self).get_context_data(**kwargs)
        context["category"] = Category.objects.all()
        return context


class ProductUpdate(LoginRequiredMixin, generic.UpdateView):
    model = Product
    template_name = "inv/products_form.html"
    context_object_name = "obj"
    form_class = ProductForm
    success_url = reverse_lazy("inv:product")
    login_url = "bases:login"

    def form_valid(self, form):
        form.instance.update_user = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        pk = self.kwargs.get('pk')
        context = super(ProductUpdate, self).get_context_data(**kwargs)
        context["category"] = Category.objects.all()
        context["obj"] = Product.objects.filter(pk=pk).first()
        return context


class ProductDelete(LoginRequiredMixin, generic.DeleteView):
    model = Product
    template_name = "inv/products_delete.html"
    context_object_name = "obj"
    success_url = reverse_lazy("inv:product")

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        return HttpResponseRedirect(self.get_success_url())