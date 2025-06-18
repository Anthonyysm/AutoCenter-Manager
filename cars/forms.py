from django import forms
from cars.models import Brand


class CarForm(forms.Form):
    model = forms.CharField()
    brand = forms.ModelChoiceField(Brand.objects.all())
    factory_year = forms.IntegerField(required=False)
    model_year = forms.IntegerField(required=False)
    plate = forms.CharField(max_length=10)
    value = forms.FloatField()
    photo = forms.ImageField()