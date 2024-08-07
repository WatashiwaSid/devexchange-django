from .models import Comment, Question
from django import forms
from ckeditor.widgets import CKEditorWidget

class CommentForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorWidget(config_name='default'))
    class Meta:
        model = Comment
        fields = ['name', 'content']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control' }),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }

class CommentFormTwo(forms.ModelForm):
    content = forms.CharField(widget=CKEditorWidget(config_name='default'))

    class Meta:
        model = Comment
        fields = ['content']

class QuestionForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorWidget(config_name='default'))  # Use CKEditorWidget for the content field

    class Meta:
        model = Question
        fields = ['title', 'content']