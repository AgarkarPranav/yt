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

def cirSectorRes(request):
	theta = float(request.GET["theta"])
	sec = float(request.GET["radiusSec"])
	resSec =  two*pi*sec*theta/360+2*sec
	act = 'active'
	idh = 'ht'
	fracSec = str(resSec)
	fractionalvalueSec = fractions.Fraction(fracSec).limit_denominator(7)
	return render(request, "perimeter/sector.html", {'activeP':act,'idep':idh,'resultSec':resSec,'fractionSec':fractionalvalueSec,'valSec':sec, 'theta':theta})


def cirSector(request):
	act = 'active'
	idh = 'ht'
	# css = 'style=color:black;'
	return render(request, "perimeter/sector.html", {'activeP':act,'idep':idh})