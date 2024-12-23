from django import forms    
from . models import Post
from django.forms import TextInput,Textarea,FileInput
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class MakePost(forms.ModelForm):
    class Meta:
        model=Post
        fields=['title','content','image']
        widgets={
            'title': TextInput(attrs={
                "class":"form-control mr-0 ml-auto",
                "name":"title",
                "id":"name",
                "type":"text"                            
            }),
            'content': Textarea(attrs={
                "class":"form-control mr-0 ml-auto",
                "name":"content",
                "id":"email",
                "type":"email"
            }),
            'image': FileInput(attrs={
                "class":"form-control mr-0 ml-auto",
                "name":"image",
                "id":"subject",
                "type":"file"
            })
        }
class CustionUserCreationForm(UserCreationForm):
    class Meta:
        model=User
        fields = ('username', 'email', 'password1',
                  'password2')
        help_texts = {
            'username':None,
            'emai':None,
        }
    def __init__(self, *args,**kwargs):
            super().__init__(*args,**kwargs)
            self.fields['password1'].help_text=''
            self.fields['password2'].help_text=''