from rest_framework import permissions

class IsStaffEditorPermission(permissions.DjangoModelPermissions):
    # gives access to the API according to the request type, and also if the permission is already set in the admin dashboard
    perms_map = {
        'GET': ['%(app_label)s.view_%(model_name)s'],
        'OPTIONS': [],
        'HEAD': [],
        'POST': ['%(app_label)s.add_%(model_name)s'],
        'PUT': ['%(app_label)s.change_%(model_name)s'],
        'PATCH': ['%(app_label)s.change_%(model_name)s'],
        'DELETE': ['%(app_label)s.delete_%(model_name)s'],
    }

    # Can also be achieved by permissions.IsAdminUser
    # def has_permission(self, request, view):
    #     if not request.user.is_staff:
    #         return False
    #     return super().has_permission(request, view)


    # def has_permission(self, request, view):
    #     user = request.user
    #     print(user.get_all_permissions())
    #     if user.is_staff:
    #         if user.has_perm("products.view_product"):  #"app_name.verb_model_name"
    #             return True
    #         if user.has_perm("products.create_product"):
    #             return True
    #         if user.has_perm("products.update_product"):
    #             return True
    #         if user.has_perm("products.delete_product"):
    #             return True
    #         return False
    #     return False