from django import forms
from .models import Post, Comment
from django.contrib.auth.models import User

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'review', 'price', 'starScore', 'image')

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)

        labels = {
            'content':'',
        }

        widgets = {
            'content':forms.Textarea(attrs={
                'placeholder':'댓글 달기',
                'size':'20'
            })
        }

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password')

        widgets = {
            'username':forms.TextInput(attrs={'placeholder':'아이디'}),
            'password':forms.PasswordInput(attrs={'placehloder':'비밀번호'})
        }