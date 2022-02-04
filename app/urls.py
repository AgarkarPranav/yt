from django.urls import path
from . import views



urlpatterns = [
	path('', views.index, name="home"),
	path('peri/', views.peri, name="peri"),
	path('peri/circle', views.circle, name="circle"),
	path('peri/circleres', views.circleres, name='circleres'),
	path('peri/circleRD', views.radiusAndDiameter, name='randD'),
	path('peri/sector', views.cirSector, name='sec'),
	path('peri/sectorRes', views.cirSectorRes, name='secres'),
]