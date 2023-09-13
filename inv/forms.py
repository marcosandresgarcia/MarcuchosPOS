from django import forms
from inv.models import Category, Product


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ["name", "state"]
        labels = {"name" : "Nombre de Categoria", "state" : "Estado"}
        widget = {"name":forms.TextInput()}

    def __int__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({'class':'form-control'})


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ["code", "name", "price", "category"]
        widget = {"name": forms.TextInput()}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })
