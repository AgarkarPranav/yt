from django.shortcuts import render
import fractions

pi = 22/7
resPi = 7/22
half = 1/2
two = 2
# Create your views here.
def index(request):
	act = 'active'
	idh = 'ht'
	# css = '.active{color:black;} .active:hover{color:white}'
	return render(request, "body.html",{'activeH': act,'ideh':idh})

def peri(request):
	act = 'active'
	idh = 'ht'
	# css = 'style=color:black;'
	return render(request, "perimeter/perimeter.html", {'activeP':act,'idep':idh})

def circle(request):
	act = 'active'
	idh = 'ht'
	# css = 'style=color:black;'
	return render(request, "perimeter/circle.html", {'activeP':act,'idep':idh})

def circleres(request):
	r = float(request.GET["radius"])
	res =  two*pi*r
	act = 'active'
	idh = 'ht'
	frac = str(res)
	fractionalvalue = fractions.Fraction(frac).limit_denominator(7)
	return render(request, "perimeter/circle.html", {'activeP':act,'idep':idh,'result':res,'fraction':fractionalvalue,'val':r})

def radiusAndDiameter(request):
	rD = float(request.GET["circumference"])
	resD =  rD*resPi*half
	act = 'active'
	idh = 'ht'
	fracD = str(resD)
	fractionalvalueD = fractions.Fraction(fracD).limit_denominator(7)
	return render(request, "perimeter/circle.html", {'activeP':act,'idep':idh,'resultD':resD,'fractionD':fractionalvalueD,'valD':rD})