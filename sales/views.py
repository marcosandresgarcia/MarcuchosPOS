from django.urls import reverse_lazy
from django.views import generic

from bases.views import UnauthorizedView, BaseCreateView, BaseDeleteView, BaseUpdateView
from sales.models import Clients
from sales.forms import ClienteForm

class ClientsView(UnauthorizedView, generic.ListView):
    permission_required = "sales.view_clients"
    model = Clients
    template_name = "sales/clients.html"
    context_object_name = "obj"


class ClientsCreate(BaseCreateView):
    model = Clients
    template_name = "sales/clients_form.html"
    form_class = ClienteForm
    success_url = reverse_lazy("sales:clients")
    permission_required = "sales.view_clients"


class ClientsUpdate(BaseUpdateView):
    model = Clients
    template_name = "sales/clients_form.html"
    form_class = ClienteForm
    success_url = reverse_lazy("sales:clients")
    permission_required = "sales.view_clients"

    def get_context_data(self, **kwargs):
        pk = self.kwargs.get('pk')
        context = super(ClientsUpdate, self).get_context_data(**kwargs)
        context["client"] = Clients.objects.all()
        context["obj"] = Clients.objects.filter(pk=pk).first()
        return context


class CategoryDelete(BaseDeleteView):
    permission_required = "sales.view_clients"
    model = Clients
    template_name = "sales/clients_delete.html"
    success_url = reverse_lazy("sales:clients")