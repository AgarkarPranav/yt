from django.shortcuts import render

# Create your views here.
def index(request):
	act = 'active'
	return render(request, "body.html",{'activeH': act})