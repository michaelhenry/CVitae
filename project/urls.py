from django.urls import (path, include)
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.authtoken.views import obtain_auth_token

from apps.CVitae.views import (

  job_list_view,
  job_detail_view,
  project_list_view,
  project_detail_view,
  company_list_view,
  company_detail_view,
  skill_list_view,
  skill_detail_view,
  profile_view,
  )

urlpatterns = [
  path('admin/', admin.site.urls),
  path('v1/token/', obtain_auth_token, name='auth-token'),
  path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]

# STATIC FILES
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# PAGES
urlpatterns += [
  path('v1/u/<slug:username>/jobs', job_list_view, name='job-list'),
  path('v1/u/<slug:username>/jobs/<int:pk>', job_detail_view, name='job-detail'),
  path('v1/u/<slug:username>/skills', skill_list_view, name='skill-list'),
  path('v1/u/<slug:username>/skills/<int:pk>', skill_detail_view, name='skill-detail'),
  path('v1/u/<slug:username>/companies', company_list_view, name='company-list'),
  path('v1/u/<slug:username>/companies/<int:pk>', company_detail_view, name='company-detail'),
  path('v1/u/<slug:username>/projects', project_list_view, name='project-list'),
  path('v1/u/<slug:username>/projects/<int:pk>', project_detail_view, name='project-detail'),
  path('v1/u/<slug:username>/', profile_view, name='profile'),
]

#DEBUG TOOLBAR
if settings.DEBUG_TOOLBAR:
  import debug_toolbar
  urlpatterns  += [
    path('__debug__/', include(debug_toolbar.urls)),
  ]


admin.site.site_header      =    'CVitae'
admin.site.site_title       =    'CVitae'
admin.site.site_url         =     None
