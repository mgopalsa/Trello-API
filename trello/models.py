from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField
from datetime import datetime
from django.utils import timezone

class Board(models.Model):
    """
    Class representing a Trello board. board attributes are stored on
    the object
    http://localhost:8080/boards/
    """
    name = models.CharField(max_length=100)
    is_active =  models.BooleanField(default=True)
    created_by = models.ManyToManyField(User)

    def __str__(self):
        return str(self.name)

class List(models.Model):
    """
    Class representing a Trello List corresponding to a board.
    List attributes are stored on the object
    http://localhost:8080/lists/
    """
    name = models.CharField(max_length=100)
    cards_order = ArrayField(models.IntegerField(), default=list)
    board = models.ForeignKey(Board, on_delete=models.CASCADE, related_name='lists')
    is_active =  models.BooleanField(default=True)
    created_by = models.ManyToManyField(User)

    def __str__(self):
        return str(self.name)

class Label(models.Model):
    """
    Class representing a Trello Label.
    Label attributes are stored on the object
    http://localhost:8080/labels/
    """
    name = models.CharField(max_length=100)
    is_active =  models.BooleanField(default=True)

    def __str__(self):
        return str(self.name)

class Card(models.Model):
    """
    Class representing a Trello Card corresponding to a board/List.
    Card attributes are stored on the object
    http://localhost:8080/cards/
    """
    title = models.CharField(max_length=100)
    list = models.ForeignKey(List, on_delete=models.CASCADE, related_name='cards')
    Description = models.CharField(max_length=100, blank=True)
    Due_date = models.DateTimeField(default=timezone.now(), blank=True)
    Label = models.ForeignKey(Label, on_delete=models.SET_NULL, related_name='Label', null = True, blank=True)
    Members = models.ManyToManyField(User, blank=True, default='')
    is_active =  models.BooleanField(default=True)

    def __str__(self):
        return str(self.title)
