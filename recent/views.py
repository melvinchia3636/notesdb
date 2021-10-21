from django.shortcuts import render
from database.models import Note

def HomeView(request):
	return render(request, 'recent/index.html', {'items': Note.objects.all().order_by("-published")[:20], 'active': 0})