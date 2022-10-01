from django import forms

from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

class CreateComment(forms.Form):
    comment_text = forms.CharField(help_text="Write your comment, don`t use insults and curses")



