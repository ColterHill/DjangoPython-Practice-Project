from django import forms
from .models import Item


class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['item_name','item_description','item_price','item_image']

        widgets = {
            'item_name': forms.TextInput(attrs={'class': 'form-control'}),
            'item_description': forms.Textarea(attrs={'class': 'form-control'}),
            'item_price': forms.NumberInput(attrs={'class': 'form-control'}),
            'item_image': forms.TextInput(attrs={'class': 'form-control'}),
        }