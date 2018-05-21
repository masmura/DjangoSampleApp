from django.urls import path

from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('/', views.index, name='index'),
	path('results/', views.results, name='results'),
	path('thanks/', views.feedback, name='thanks'),
]
