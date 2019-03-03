from rest_framework import generics

from .models import Board, List, Card, Label
from .serializers import BoardListSerializer, BoardDetailSerializer, \
 ListSerializer, CardSerializer, LabelSerializer, UserSerializer
from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import PermissionDenied

class BoardList(generics.ListCreateAPIView):
    queryset = Board.objects.filter(is_active=True)
    serializer_class = BoardListSerializer

class BoardDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Board.objects.filter(is_active=True)
    serializer_class = BoardDetailSerializer

    """
    Override destroy function to ensure that only the creator can delete the Board.
    Otherwise retyrn a Permission denied warning.
    """
    def destroy(self, request, *args, **kwargs):
        board = Board.objects.get(pk=self.kwargs["pk"])
        if not request.user == board.created_by:
            raise PermissionDenied("You can not delete this Board.")
        return super().destroy(request, *args, **kwargs)

class ListList(generics.ListCreateAPIView):
    queryset = List.objects.filter(is_active=True)
    serializer_class = ListSerializer

class ListDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = List.objects.all()
    serializer_class = ListSerializer

    """
    Override destroy function to ensure that only the creator can delete the List.
    Otherwise retyrn a Permission denied warning.
    """
    def destroy(self, request, *args, **kwargs):
        list = List.objects.get(pk=self.kwargs["pk"])
        if not request.user == list.created_by:
            raise PermissionDenied("You can not delete this List.")
        return super().destroy(request, *args, **kwargs)

class CardList(generics.ListCreateAPIView):
    queryset = Card.objects.filter(is_active=True)
    serializer_class = CardSerializer

class CardDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Card.objects.all()
    serializer_class = CardSerializer

    """
    Override destroy function to ensure that only the creator can delete the Card.
    Otherwise retyrn a Permission denied warning.
    """
    def destroy(self, request, *args, **kwargs):
        card = Card.objects.get(pk=self.kwargs["pk"])
        if not request.user == card.Members:
            raise PermissionDenied("You can not delete this Card.")
        return super().destroy(request, *args, **kwargs)

class LabelList(generics.ListCreateAPIView):
    queryset = Label.objects.filter(is_active=True)
    serializer_class = LabelSerializer

class LabelDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Label.objects.all()
    serializer_class = LabelSerializer

class UserCreate(generics.CreateAPIView):
    authentication_classes = ()
    permission_classes = ()
    serializer_class = UserSerializer

"""
Class representing a Trello API Login.
Returns the Token on posting username and password
http://localhost:8080/login/
"""
class LoginView(APIView):
    permission_classes = ()

    def post(self, request,):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(username=username, password=password)
        if user:
            return Response({"token": user.auth_token.key})
        else:
            return Response({"error": "Wrong Credentials"}, status=status.HTTP_400_BAD_REQUEST)
