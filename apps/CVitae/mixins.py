from apps.common.permissions import (IsObjectOwner, ReadOnly)


class CVitaeViewsetBasicsMixin(object):

  def get_username(self):
    return self.kwargs.get('username')

  def get_permissions(self):

    if self.request.user.is_authenticated \
      and self.get_username()== self.request.user.username:
        permission_classes = [IsObjectOwner]
    else:
        permission_classes = [ReadOnly]
    return [permission() for permission in permission_classes]

  def perform_create(self, serializer):
    serializer.save(created_by=self.request.user)

  def get_serializer_context(self):
    return {'request': self.request}

