from rest_framework import viewsets
from .mixins import CVitaeViewsetBasicsMixin
from .models import (
  Job, 
  Project, 
  Company, 
  Profile, 
  Skill)
from .serializers import (
  JobSerializer, 
  ProjectSerializer, 
  CompanySerializer, 
  ProfileSerializer, 
  SkillSerializer)


class JobViewSet(CVitaeViewsetBasicsMixin, viewsets.ModelViewSet):

  serializer_class = JobSerializer

  def get_queryset(self):
    return Job.objects.filter(created_by__username=self.get_username())


class ProjectViewSet(CVitaeViewsetBasicsMixin, viewsets.ModelViewSet):

  serializer_class = ProjectSerializer

  def get_queryset(self):
    return Project.objects.filter(created_by__username=self.get_username())


class CompanyViewSet(CVitaeViewsetBasicsMixin, viewsets.ModelViewSet):

  serializer_class = CompanySerializer

  def get_queryset(self):
    return Company.objects.filter(created_by__username=self.get_username())


class SkillViewSet(CVitaeViewsetBasicsMixin, viewsets.ModelViewSet):
  
  serializer_class = SkillSerializer

  def get_queryset(self):
    return Skill.objects.filter(created_by__username=self.get_username())


class ProfileViewSet(CVitaeViewsetBasicsMixin, viewsets.ModelViewSet):

  serializer_class = ProfileSerializer
  queryset = Profile.objects.all()

  def get_object(self):
    obj = self.get_queryset().get(created_by__username=self.get_username())
    return obj



job_list_view = JobViewSet.as_view({
  'get' : 'list',
  'post' : 'create',
})

job_detail_view = JobViewSet.as_view({
  'get'   :   'retrieve',
  'put'   :   'update',
  'patch' :   'partial_update',
  'delete':   'destroy',
})

project_list_view = ProjectViewSet.as_view({
  'get' : 'list',
  'post' : 'create',
})

project_detail_view = ProjectViewSet.as_view({
  'get'   :   'retrieve',
  'put'   :   'update',
  'patch' :   'partial_update',
  'delete':   'destroy',
})

company_list_view = CompanyViewSet.as_view({
  'get' : 'list',
  'post' : 'create',
})

company_detail_view = CompanyViewSet.as_view({
  'get'   :   'retrieve',
  'put'   :   'update',
  'patch' :   'partial_update',
  'delete':   'destroy',
})

skill_list_view = SkillViewSet.as_view({
  'get' : 'list',
  'post' : 'create',
})

skill_detail_view = SkillViewSet.as_view({
  'get'   :   'retrieve',
  'put'   :   'update',
  'patch' :   'partial_update',
  'delete':   'destroy',
})

profile_view = ProfileViewSet.as_view({
  'get'   : 'retrieve',
  'put'   :   'update',
  'patch' :   'partial_update',
})