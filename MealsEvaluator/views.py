from django.shortcuts import render
from rest_framework import viewsets
from .models import Meal, Rating
from .serializers import MealSerializer, RatingSerializer

class Meal_View(viewsets.ModelViewSet):
    queryset = Meal.objects.all()
    serializer_class = MealSerializer
        
                 
class Rating_View(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer

