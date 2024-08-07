from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor.fields import RichTextField

# Create your models here.

class Question(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=500)
    content = RichTextField()
    date_created = models.DateTimeField(default=timezone.now)
    

    def __str__(self):
        return f"{self.user.username} -{self.title[:100]}"
    
    def get_absolute_url(self):
        return reverse("stackbase:questionDetail", kwargs={"pk": self.pk})

class Comment(models.Model):
    question = models.ForeignKey(Question, related_name='comments', on_delete=models.CASCADE) 
    name = models.CharField(max_length=200)
    content = RichTextField()
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return '%s %s' % (self.question.title, self.question.user)
    
    def get_absolute_url(self):
        return reverse("stackbase:questionDetail", kwargs={"pk": self.pk})
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
