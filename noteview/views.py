from django.shortcuts import render, get_object_or_404
from database.models import Note

# Create your views here.
def HomeView(request, subject, id):
	return render(request, 'view/index.html', {"note": get_object_or_404(Note, subject__id=subject, id=id)})
