'''
Created on 2018. 11. 4.

@author: user
'''

from django.forms.models import ModelForm
from .models import Post
class PostForm(ModelForm):
    
    files = forms.FileField(required=False, widget=forms.ClearableFileinput(attrs={'multiple':True}))
    image = forms.FileField(required=False, widget=forms.ClearableFileinput(attrs={'multiple':True}))
    class Meta:
        model = Post
        fields=['type','headline','content']