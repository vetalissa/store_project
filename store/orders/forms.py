from django import forms
from orders.models import Order


class OrderForm(forms.ModelForm):
    # address = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-title', 'style': "width: 100%;"}))

    class Meta:
        model = Order
        fields = ('address',)
