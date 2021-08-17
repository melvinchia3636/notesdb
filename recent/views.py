from django.shortcuts import render
from database.models import Note

def HomeView(request):
	return render(request, 'recent/index.html', {'items': Note.objects.all()[:20], 'active': 0})