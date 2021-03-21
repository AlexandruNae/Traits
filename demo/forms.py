from django import forms
from .models import AuthUser as User, Post

class PostForm(forms.ModelForm):

    class Meta:
        model = User
        fields = "__all__"

class Postare(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['id_user_poster','id_user_posted','titlu','text','good_bad']
