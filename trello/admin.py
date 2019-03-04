from django.contrib import admin

from .models import Board, List, Card, Label

admin.site.site_header = "Trello Admin"
admin.site.site_title = "Trello Admin Portal"
admin.site.index_title = "Welcome to Trello tool Portal"

admin.site.register(Board)
admin.site.register(List)
admin.site.register(Card)
admin.site.register(Label)
