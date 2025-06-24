from django import forms
from cars.models import Brand, Car


class CarForm(forms.Form):
    model = forms.CharField()
    brand = forms.ModelChoiceField(Brand.objects.all())
    factory_year = forms.IntegerField(required=False)
    model_year = forms.IntegerField(required=False)
    plate = forms.CharField(max_length=10)
    value = forms.FloatField()
    photo = forms.ImageField()

    def save(self):
        car = Car(
            model = self.cleaned_data['model'],
            brand = self.cleaned_data['brand'],
            factory_year = self.cleaned_data['factory_year'],
            model_year = self.cleaned_data['model_year'],
            plate = self.cleaned_data['plate'],
            value = self.cleaned_data['value'],
            photo = self.cleaned_data['photo'],
        )
        car.save()
        return car
    
class CarModelForm(forms.ModelForm):

    class Meta:
        model = Car
        fields = '__all__'