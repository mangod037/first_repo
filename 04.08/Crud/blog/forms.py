from django import forms
from .models import Post
#from .models import ScoreChoice

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'review', 'price', 'starScore')

# class ChiceForm(forms.ModelForm):
#     starScore = forms.ChoiceField(label="", initial='', widget=forms.Select(), required=True)

#     class Meta:
#         model = ScoreChoice
#         fields = ('score')


