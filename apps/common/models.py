from django.db import models
from django.conf import settings


class HasTimeStampedModel(models.Model):

  created   =  models.DateTimeField(auto_now_add=True)
  modified  =  models.DateTimeField(auto_now=True)

  class Meta:
    abstract = True


class HasOwnershipInfoModel(HasTimeStampedModel):

  created_by = models.ForeignKey(
    settings.AUTH_USER_MODEL,
    related_name='%(class)s_all',
    on_delete=models.CASCADE,
    null=True,
    blank=True,
  )

  modified_by = models.ForeignKey(
    settings.AUTH_USER_MODEL,
    on_delete=models.SET_NULL,
    null=True,
    blank=True,
  )

  class Meta(object):
    abstract = True
