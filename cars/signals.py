from django.db.models.signals import post_delete, post_save
from django.dispatch import receiver
from cars.models import Car
from django.db.models import Sum


@receiver(post_save, sender=Car)
def car_post_save(sender, instance, **kwargs):
    cars_caunt = Car.objects.all().count()
    cars_value = Car.objects.aggregate(
        total_value = Sum('value')
    )


@receiver(post_delete, sender=Car)
def car_post_delete(sender, instance, **kwargs):
    ...
