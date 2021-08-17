from django.shortcuts import render

def HomeView(request):
	return render(request, 'profile/index.html')