from django import forms
from catalog.models import Product, Version, Category
from django.shortcuts import redirect


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class CategoryForm(StyleFormMixin, forms.ModelForm):
    model = Category
    exclude = '__all__'


class ProductForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Product
        exclude = ('owner',)

    def clean_product_name(self):
        cleaned_data = self.cleaned_data['product_name']
        cleaned_list = cleaned_data.replace('.', '').split()

        forbidden_words = (
            'казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар')
        for word in cleaned_list:
            if word in forbidden_words:
                raise forms.ValidationError('Недопустимые слова/символы')
        return cleaned_data

    def clean_description(self):
        cleaned_data = self.cleaned_data['description']
        cleaned_list = cleaned_data.replace('.', '').split()

        forbidden_words = (
            'казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар')
        for word in cleaned_list:
            if word in forbidden_words:
                raise forms.ValidationError('Недопустимые слова/символы')
        return cleaned_data


class VersionForm(forms.ModelForm):
    class Meta:
        model = Version
        fields = '__all__'
