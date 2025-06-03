from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from apps.tickets.models import Ticket
from apps.finance.models import Finance
from apps.blog.models import Blog
from apps.account.models import User


groups = {
    'support_ticket':['view_ticket','answer_ticket','edit_ticket','delete_ticket'] ,
    'support_finance' :['check_payment','confirmation_payment','Rejectـpayment'] ,
    'support_blog' :['add_text','edit_text','delete_text','add_file'],
    'superuser':'all'
}

for group_name , perms in groups.items():
    group, _ = Group.objects.aget_or_create(name=group_name)

    if perms == 'all' :
        all_perms = Permission.objects.all()
        group.permissions.set(all_perms)
        continue

    group_permissions  = []
    for perm_codename in perms:
        perm = Permission.objects.get(codename=perm_codename)
        group_permissions.append(perm)
    
    group.permissions.set(group_permissions)
    group.save()
print("Groups and permissions created.")
