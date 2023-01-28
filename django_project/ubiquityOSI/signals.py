# from django.db.models.signals import post_save
# from django.contrib.auth.models import User
# from django.dispatch import receiver
# from .models import PostServices
#
#
# @receiver(post_save, sender=User)
# def create_service_pic(sender, instance, created, **kwargs):
#     if created:
#         ServiceProvidersPics.objects.create(user=instance)
#
#
# @receiver(post_save, sender=User)
# def save_service_pic(sender, instance, **kwargs):
#     instance.post_services.save()