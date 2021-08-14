from django.shortcuts import render

def HomeView(request):
	return render(request, 'starred/index.html')