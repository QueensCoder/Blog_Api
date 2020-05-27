from rest_framework import permissions

# new comments
# custom permission creation
# test


class IsAuthorOrReadOnly(permissions.BasePermission):
    # need to overwrite permission classses that basepermisions has
    # this method determins if the request methods are safe methods
    # if not it checks to make sure a user issuing unsafe methods
    # is only the author of the post
    def has_object_permission(self, req, view, obj):
        if req.method in permissions.SAFE_METHODS:
            return True
        return obj.author == req.user
