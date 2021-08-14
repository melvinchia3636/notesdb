from django.shortcuts import render

def HomeView(request):
	return render(request, 'my_contributions/index.html')