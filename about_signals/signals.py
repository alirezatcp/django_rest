from django.db.models.signals import post_save
from django.dispatch import receiver

from about_signals.models import Product

# using logger (default showing more than debug logs)
import logging

logger = logging.getLogger(__name__)

# post_save: exec after calling create methode for a model 
@receiver(post_save, sender=Product)
def tell_people(sender, instance, created, **kwargs):
    if created:
        logger.warning(f'Product created: {instance.name} with price {instance.price}')

    else:
        logger.critical("Product didnt created!!!!")


# pre_save: exec before calling create methode for a model
# @receiver(pre_save, sender=Product)
# def tell_people(sender, instance, **kwargs):

# m2m_changed: execute when a ManyToManyField changes in a model: (here we don't have manytomany field.)
# @receiver(m2m_changed, sender=model_name.ManyToManyField_name.through)
# def do_something(sender, instance, action, reverse, **kwargs):