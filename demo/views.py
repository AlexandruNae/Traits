import datetime

from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.template.response import TemplateResponse
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from .models import AuthUser as User, Post
from .serializers import UserSerializer, PostSerializer


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

class PostViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

def show_html(request):
    users = User.objects.all()
    return render(request,'first_temp.html', {'data':users})

def index(request):
    user_id = request.user.id

    return render(request, 'base.html', {'user_id': user_id})

def logout_user(request):
    return render(request, 'logout_user.html',{})

def home(request):
    print(request.user)
    return render(request, 'home.html',{})

def user_list(request):
    users = User.objects.all()
    print(users)
    return render(request, 'user_list.html',{'users':users})

def formular(request):
    return render(request,'formular.html', {'data':'Completeazaa aicii cu dinamicile tale'})

def my_user_wall(request, template_name='my_user_wall.html'):
    user = request.user
    return TemplateResponse(request,template_name, {'user':user})

def wall2(request):
    return render(request, "wall.html")

def wall(request, user_id):
    user_auth = request.user
    user = User.objects.get(id=user_id)
    posts = Post.objects.raw('SELECT * FROM  good_bad.post WHERE id_user_posted = %s', [user.id])

    return render(request,"wall.html", {'user':user, 'posts':posts, 'user_auth':user_auth})

def delete_post(request,post_id):
    post_to_delete = Post.objects.get(id_postare=post_id)
    post_to_delete.delete()
    user_wall = post_to_delete.id_user_posted
    return redirect("/wall/" + str(user_wall.id))


def add_1(request):

    print("IN afara ifulurli")
    if request.method == 'POST':
        print("intre ifuri")
        print("in if")

        new_post = Post()
        new_post.titlu = request.POST.get("titlu")
        new_post.text = request.POST.get("text")
        new_post.good_bad = int(request.POST.get("good_bad"))

        user = request.user
        user_id = user.id
        user_poster = User.objects.get(id=user_id)
        new_post.id_user_poster = user_poster

        print(request.POST.get("posted"))

        user_posted_id = request.POST.get("posted")
        user_posted = User.objects.get(id=user_posted_id)
        new_post.id_user_posted = user_posted

        print(new_post)

        new_post.save()
        print("in if")

        return redirect("/wall/" + str(user_posted_id))

    else:
        print("in else")
        return render(request, "wall.html")