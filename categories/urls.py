from django.urls import path
from . import views

urlpatterns = [
	path('', views.HomeView, name="categories"),
	path('<str:type>/<uuid:id>', views.CategoryView, name="category")
]