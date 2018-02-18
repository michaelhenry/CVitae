from rest_framework import serializers
from .models import (Job, Project, Company, Profile, Skill)

class JobSerializer(serializers.ModelSerializer):


  class Meta:
    model = Job
    fields = (
      'id', 
      'name', 
      'description',
      'company',
      )
 


class ProjectSerializer(serializers.ModelSerializer):

  class Meta:
    model = Project
    fields = (
      'id', 
      'name', 
      'description',
      'start_date',
      'end_date',
      'photo',
      )


class CompanySerializer(serializers.ModelSerializer):

  class Meta:
    model = Company
    fields = (
      'id', 
      'name', 
      'description',
      )


class SkillSerializer(serializers.ModelSerializer):

	class Meta:
		model = Skill
		fields = (
			'id', 
			'name', 
			'description',
      'level',
			)


class ProfileSerializer(serializers.ModelSerializer):

 
  class Meta:
    model = Profile
    fields = (
      'id', 
      'display_name', 
      'job_title',
      'email',
      )