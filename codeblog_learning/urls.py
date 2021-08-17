from django.conf.urls import include, url
from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render
from django.conf import settings
from django.views.static import serve

def page_not_found(request, exception):
    return render(request, 'base/page_not_found.html')

def server_error(request):
    return render(request, 'base/internal_error.html')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('recent.urls')),
    path('recent/', include('recent.urls')),
    path('statistic/', include('statistic.urls')),
    path('starred/', include('starred.urls')),
    path('categories/', include('categories.urls')),
    path('download/', include('download.urls')),
    path('profile/', include('profile.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('view/', include('noteview.urls'))
]

handler404 = 'codeblog_learning.urls.page_not_found'
handler500 = 'codeblog_learning.urls.server_error'

import django.views.static
urlpatterns += [
    url(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
    url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
]