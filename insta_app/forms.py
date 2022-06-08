
from django import forms
from .models import Comment






class PostCommentForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(PostCommentForm, self).__init__(*args, **kwargs)
        self.fields['content'].widget.attrs.update({'placeholder':'Add comments...'})
    class Meta:
        model = Comment
        fields = ['content']

    