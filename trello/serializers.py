from rest_framework import serializers
from django.contrib.auth.models import User

from .models import Board, List, Card, Label
from rest_framework.authtoken.models import Token


"""
Below for loop takes care of the Token creation
on each new user creation
"""
for user in User.objects.all():
    Token.objects.get_or_create(user=user)


class CardSerializer(serializers.ModelSerializer):
    """
    Each specific Card attributes can be fetched here.
    http://localhost:8080/cards/<pk>
    """
    class Meta:
        model = Card
        fields = ('id', 'title', 'list','Description', 'Due_date', 'Label', 'Members', 'is_active')

class LabelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Label
        fields = ('id', 'name', 'is_active')

class ListSerializer(serializers.ModelSerializer):
    cards = CardSerializer(many=True, read_only=True)
    """
    Each specific Board attributes can be fetched here.
    http://localhost:8080/lists/<pk>
    """
    class Meta:
        model = List
        fields = ('id', 'name', 'cards_order', 'board', 'cards', 'is_active')

class BoardListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Board
        fields = ('id', 'name', 'is_active')

class BoardDetailSerializer(serializers.ModelSerializer):
    lists = ListSerializer(many=True, read_only=True)
    """
    Each specific Board attributes can be fetched here.
    http://localhost:8080/boards/<pk>
    """
    class Meta:
        model = Board
        fields = ('id', 'name', 'is_active', 'lists')

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        Token.objects.create(user=user)
        return user
