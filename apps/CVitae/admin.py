from django.contrib import admin
from .models import (Job, Project, Company, Profile, Skill)


class ExcludeMetaInfo(object):

  exclude = ('created_by', 'modified_by',)


class AutoSaveUserInfo(object):

  def save_model(self, request, obj, form, change):

    try:
      if change:
        obj.modified_by = request.user
      else:
        obj.created_by = request.user
      obj.save()
    except:
      print("error on saving user info.")


class ProjectTabularInlineModelAdmin(admin.TabularInline):

  exclude = ('start_date', 'end_date', ) + ExcludeMetaInfo.exclude
  model = Project
  extra = 1

class OnlyShowOwnData(object):

  def get_queryset(self, request):
    qs = super(OnlyShowOwnData, self).get_queryset(request)
    return qs.filter(created_by=request.user)


class JobAdmin(OnlyShowOwnData, ExcludeMetaInfo, AutoSaveUserInfo, admin.ModelAdmin):

  ordering            =    ('name',)
  search_fields       =    ('name','description',)
  list_display        =    ('name' ,'description', 'start_date', 'end_date',)
  inlines             =    [ProjectTabularInlineModelAdmin,]
  autocomplete_fields =    ['company',]

  def save_model(self, request, obj, form, change):

    # Save inline projects
    for project in obj.projects.all():
      if not project.created_by:
        project.created_by = request.user
      else:
        project.modified_by = request.user
      project.save()
    return super(JobAdmin, self).save_model(request, obj, form, change)
    

class ProjectAdmin(OnlyShowOwnData, ExcludeMetaInfo, AutoSaveUserInfo, admin.ModelAdmin):

  ordering            =    ('name',)
  search_fields       =    ('name','description',)
  list_display        =    ('name' ,'description', 'start_date', 'end_date',)


class CompanyAdmin(OnlyShowOwnData, ExcludeMetaInfo, AutoSaveUserInfo, admin.ModelAdmin):

  ordering            =    ('name',)
  search_fields       =    ('name','description',)
  list_display        =    ('name' ,'description',)


class SkillAdmin(OnlyShowOwnData, ExcludeMetaInfo, AutoSaveUserInfo, admin.ModelAdmin):

  ordering            =    ('name',)
  search_fields       =    ('name','description',)
  list_display        =    ('name' ,'description',)


class ProfileAdmin(admin.ModelAdmin):

  # Just a hack for now.
  ordering        = ('display_name',)
  search_fields   = ('display_name', 'job_title',)
  list_display    = ('display_name', 'job_title',)
  exclude = ('created_by',)

  def get_queryset(self, request):
    qs = super(ProfileAdmin, self).get_queryset(request)
    return qs.filter(created_by=request.user)

  def has_add_permission(self, request):
    return not Profile.objects.filter(created_by=request.user).exists()

  def save_model(self, request, obj, form, change):

    try:
      obj.created_by = request.user
      obj.save()
    except:
      print("error on saving profile info.")

admin.site.register(Job, JobAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Company, CompanyAdmin)
admin.site.register(Profile, ProfileAdmin)
admin.site.register(Skill, SkillAdmin)