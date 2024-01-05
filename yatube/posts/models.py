from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()

class Post(models.Model):
    text = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='posts')
    group = models.ForeignKey(to='Group', on_delete=models.DO_NOTHING, blank=True, null=True)


class Group(models.Model):
    title = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=50, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'{self.title}'