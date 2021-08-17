from django.shortcuts import render
from database.models import Subject, Grade

def HomeView(request):
	return render(request, 'categories/index.html', {
		'active': 2, 
		'subjects': Subject.objects.all(),
		'grades': Grade.objects.all()
	})