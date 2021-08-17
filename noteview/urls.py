from django.urls import path
from . import views

urlpatterns = [
	path('<uuid:subject>/<uuid:id>/', views.HomeView, name="noteview")
]