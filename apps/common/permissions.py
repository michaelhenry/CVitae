from rest_framework.permissions import IsAuthenticated, BasePermission, SAFE_METHODS


class IsObjectOwner(IsAuthenticated):

  def has_object_permission(self, request, view, obj):
    if request.method in SAFE_METHODS:
      return True
    if hasattr(obj, 'created_by'):
      return obj.created_by == request.user
    return False


class ReadOnly(BasePermission):

  def get_readonly_methods(self):
    return ['GET', 'HEAD', 'OPTIONS']

  def has_permission(self, request, view):
    if request.method in self.get_readonly_methods():
      return True
    return False

  def has_object_permission(self, request, view, obj):
    print(request.method)
    
    if request.method in self.get_readonly_methods():
      return True
    return False


class IsAuthenticatedOrOptionsRequest(IsAuthenticated):
  """
  If it is authenticated or options request.
  """

  def has_permission(self, request, view):
    if request.method == 'OPTIONS':
      return True
    return super(IsAuthenticatedOrOptionsRequest, self).has_permission(request, view)