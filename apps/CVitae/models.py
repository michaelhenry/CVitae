from django.db import models
from django.db.models.signals import post_save
from django.conf import settings
from django.dispatch import receiver
from apps.common.models import (HasOwnershipInfoModel)


class CVitaeBaseModel(HasOwnershipInfoModel):

  name        =  models.CharField(max_length=50)
  description =  models.TextField(
    max_length=200, 
    blank=True, 
    null=True)

  class Meta(object):
    abstract = True

  def __str__(self):
    return "%s" % self.name

  def __unicode__(self):
    return '%s' % self.name


class HasDateRange(models.Model):

  start_date  = models.DateField(blank=True, null=True)
  end_date    = models.DateField(blank=True, null=True)

  class Meta:
    abstract = True


class Company(CVitaeBaseModel):

  address =  models.TextField(
    max_length=200, 
    blank=True, 
    null=True)

  class Meta(object):
    verbose_name        =    'Company'
    verbose_name_plural =    'Companies'


class Job(HasDateRange, CVitaeBaseModel):

  company = models.ForeignKey(Company,
    on_delete=models.SET_NULL,
    blank=True,
    null=True,)


class Project(HasDateRange, CVitaeBaseModel):

  job = models.ForeignKey(Job, 
    related_name='projects',
    on_delete=models.CASCADE,
    blank=True,
    null=True,)

  photo = models.ImageField(blank=True, null=True, upload_to='photos/projects/')


class Skill(CVitaeBaseModel):

  level = models.IntegerField(null=True, blank=True)


class Profile(models.Model):
  created_by    = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
  display_name  = models.CharField(max_length=50)
  job_title     = models.CharField(max_length=100, null=True, blank=True)
  bio           = models.TextField(max_length=1000, blank=True)
  birth_date    = models.DateField(null=True, blank=True)
  email         = models.CharField(max_length=50, null=True, blank=True)

  def __str__(self):
    return "%s" % self.display_name

  def __unicode__(self):
    return '%s' % self.display_name
  

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_user_profile(sender, instance, created, **kwargs):
  if created:
    Profile.objects.create(created_by=instance, display_name='Unnamed')

