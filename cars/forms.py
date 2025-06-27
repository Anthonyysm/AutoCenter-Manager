from re import match
from django import forms
from cars.models import Car


class CarModelForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__'

    def clean_value(self):
        value = self.cleaned_data.get('value')
        if value < 15000:
            self.add_error(
                'value', 'Valor mínimo do carro deve ser de R$15.000')
        return value

    def clean_factory_year(self):
        factory_year = self.cleaned_data.get('factory_year')
        if factory_year < 1975:
            self.add_error(
                'factory_year', 'Carros com ano de lançamento inferior a 1975 não são aceitos')
        return factory_year

    def clean_plate(self):
        plate = self.cleaned_data.get('plate')
        if not match(r'^[A-Z]{3}-[0-9]{4}', plate) and not match(r'[A-Z]{3}[0-9]{1}[A-Z]{1}[0-9]{2}', plate):
            self.add_error(
                'plate', 'Formato de placa inválido! Digite no formato brasileiro (AAA-0000) ou no formato mercosul (AAA0A00)')
        return plate
