from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.http import Http404
from database.models import Subject, Grade, Note

def HomeView(request):
	return render(request, 'categories/index.html', {
		'active': 2, 
		'subjects': Subject.objects.all(),
		'grades': Grade.objects.all()
	})
	
def CategoryView(request, type, id):
	if type not in ['subject', 'grade']: raise Http404
	type_item = get_object_or_404(Subject if type == "subject" else Grade, id=id)
	items = get_list_or_404(Note, **{type: type_item})
	return render(request, 'categories/category.html', {'items': items, "type_item": type_item})