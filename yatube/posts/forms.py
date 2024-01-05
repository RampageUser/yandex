from django import forms
from .models import Post, Group
from django.forms import widgets



class CreatePost(forms.ModelForm):
    queryset = Group.objects.all()
    text = forms.CharField(widget=widgets.Textarea, label='Текст поста', required=True)
    group = forms.ModelChoiceField(queryset=queryset, label='Выберите группу', required=False)

    class Meta:
        model = Post
        fields = ('text', 'group')
