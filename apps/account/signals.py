from django.db.models.signals import post_migrate
from django.dispatch import receiver
from django.contrib.auth.models import Group

@receiver(post_migrate)
def create_default_groups(sender , **kwargs):
    """After migrate, this function is executed and makes sure the groups exist.
    """
    groum_names=['support','superuser']
    for name in groum_names:
        Group.objects.get_or_create(name=name)
