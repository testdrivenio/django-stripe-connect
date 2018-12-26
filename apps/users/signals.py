from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import CustomUser, Buyer, Seller


@receiver(post_save, sender=CustomUser)
def user_save(sender, instance, created, **kwargs):
    if created:
        if instance.is_seller:
            Seller.objects.create(user=instance)
        else:
            Buyer.objects.create(user=instance)
    if not created:
        user_id = instance.id
        is_buyer = Buyer.objects.filter(user=user_id).first()
        is_seller = Seller.objects.filter(user=user_id).first()
        if instance.is_seller and is_buyer:
            is_buyer.delete()
            Seller.objects.create(user=instance)
        if not instance.is_seller and is_seller:
            is_seller.delete()
            Buyer.objects.create(user=instance)
