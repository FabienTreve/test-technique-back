from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import Review

@receiver(pre_save, sender=Review)
def validate_grade(sender, instance, **kwargs):
    if instance.grade > 5:
        instance.grade = 5
    elif instance.grade < 1:
        instance.grade = 1
