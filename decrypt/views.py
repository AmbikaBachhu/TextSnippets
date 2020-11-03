from django.shortcuts import render,redirect
from django.contrib import messages
# Create your views here.
from .models import Snippet
from .forms import snippetforms
from .serializers import SnippetSerializer, UserSerializer
from rest_framework.viewsets import ModelViewSet
from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token


class Snippetviewset(ModelViewSet):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    authentication_classes = [JSONWebTokenAuthentication, ]
    permission_classes = [IsAuthenticated, ]


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    for user in User.objects.all():
        Token.objects.get_or_create(user=user)


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


def ShowDetails(request):
    context = {"detail": snippetforms()}
    return render(request, "template.html", context)


def ShowDetailsSave(request):
    saving = snippetforms(request.POST)
    saving.save()
    return redirect('show')
