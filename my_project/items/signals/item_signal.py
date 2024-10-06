from django.db.models.signals import post_save
from django.dispatch import receiver
from items.models.item_model import Item

@receiver(post_save, sender=Item)
def notify_user(sender, instance, created, **kwargs):
    if created:
        print(f'New item "{instance.name}" created by {instance.created_by.username}.')
        # You could extend this to send an email or log the event in a more sophisticated way.
