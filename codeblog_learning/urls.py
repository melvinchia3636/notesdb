from django.conf.urls import include, url
from django.contrib import admin
from django.urls import path, include
import django
from django.shortcuts import render
from django.conf import settings

def page_not_found(request, exception):
    return render(request, 'base/page_not_found.html')

def server_error(request):
    return render(request, 'base/internal_error.html')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('home/', include('home.urls')),
    path('statistic', include('statistic.urls')),
    path('recent', include('recent.urls')),
    path('starred', include('starred.urls')),
    path('categories', include('categories.urls')),
    path('download', include('download.urls')),
    path('my_contributions', include('my_contributions.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
]

handler404 = 'codeblog_learning.urls.page_not_found'
handler500 = 'codeblog_learning.urls.server_error'

import django.views.static
urlpatterns += [
   url(r'^static/(?P<path>.*)$', django.views.static.serve, {'document_root': settings.STATIC_ROOT, 'show_indexes': settings.DEBUG})
]