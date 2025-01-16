from rest_framework import serializers
from .models import Meal, Rating
from django.contrib.auth.models import User

class MealSerializer(serializers.ModelSerializer):
    author = serializers.SerializerMethodField()

    class Meta:
        model = Meal
        fields = ('id', 'title', 'description', 'user', 'author')

    def get_author(self, obj):
        user = User.objects.get(id=obj.user_id)
        return user.username
        
class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ('id', 'meal', 'user', 'stars')