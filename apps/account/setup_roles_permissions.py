from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from django.apps import apps

def creat_group_with_perms(group_name , model_names):
    group, _ = Group.objects.get_or_create(name=group_name)
    for model_name in model_names :
        try:
            model = apps.get_model(app_label=model_name["app"] , model_name=model_name["model"])
            Content_type = ContentType.objects.get_for_model(model)
            perms = Permission.objects.filter(Content_type=Content_type)
            group.permissions.set(list(group.permissions.all()) | list(perms))
        except LookupError:
            print(f"[!] Model {model_name['model']} in app {model_name['app']} not found.")
    group.save()
    print(f"[✓] Group '{group_name}' setup completed.")

def setup_roles_permissions():
    all_models = [
        {"app":"users","model":"user"},
        {"app": "finance","model":"Finance"},
        {"app": "tickets","model":"Ticket"},
        {"app":"blog","model":"Post"},
    ]
    creat_group_with_perms("superuser", all_models)    


    creat_group_with_perms("support_finance", [{"app": "finance", "model": "Finance"}])
    creat_group_with_perms("support_ticket", [{"app": "tickets", "model": "Ticket"}])
    creat_group_with_perms("support_blog", [{"app": "blog", "model": "Post"}])

setup_roles_permissions()

