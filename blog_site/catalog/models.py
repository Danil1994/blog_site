from datetime import datetime
from django.db import models
from django.urls import reverse
from django.forms import ModelForm

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
    publish_date = models.DateField('pubdate', default=datetime.today(), auto_now_add=False)
    description = models.TextField(max_length=2000, blank=False, help_text="Write your massege")

    def __str__(self):
        """
        String for representing the Model object.
        """
        return self.title

    class Meta:
        ordering =['-publish_date']

    def get_absolute_url(self):
        """
        Returns the url to access a particular instance of the model.
        """
        return reverse('post-detail', args=[str(self.id)])

class Author(models.Model):
    name = models.CharField(max_length=20)
    info = models.TextField('authors_info', max_length=200, null=True, help_text="About you...")

    def __str__(self):
        """
        String for representing the Model object.
        """
        return self.name

    def get_absolute_url(self):
        """
        Returns the url to access a particular instance of the model.
        """
        return reverse('author-detail', args=[str(self.id)])

class Comment(models.Model):
    comment_text = models.TextField(max_length=1000, help_text="Write your comment, don`t use insults and curses")
    post = models.ForeignKey('Post', on_delete=models.SET_NULL, null=True)
    publish_date = models.DateField('pubdate', default=datetime.today(), auto_now_add=False)

    def __str__(self):
        """
        String for representing the Model object.
        """
        return self.comment_text[:75]

    class Meta:
        ordering =['publish_date']


