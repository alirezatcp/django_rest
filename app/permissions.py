# add a custom permission

from rest_framework.permissions import BasePermission, SAFE_METHODS

from security.models import Blacklist # a model we created

class Blacklisted(BasePermission):
    def has_permission(self, request, view):
        ip_address = request.META['REMOTE_ADDR']
        in_blacklist = Blacklist.objects.filter(ip = ip_address).exists()
        return not in_blacklist
# to use this permission just add it in permission_classes in view.


# this permission allow users read but they can modify gust when they are author of a post.
class IsAuthorOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        # SAFE_METHODS: ['GET', 'HEAD', 'OPTIONS']
        if request.method in SAFE_METHODS:
            return True

        return obj.author == request.user
# to use this permission we should add it in permission_classes in view and we should use check_object_permissions method in post, put, ... too:
# article = get_object_ot_404(Article, id=article_id)
# self.check_object_permissions(request, article)