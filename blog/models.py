from django.db import models
from django.utils.timezone import now

class BlogProject(models.Model):
    blog_title = models.CharField(max_length=100)
    date = models.DateTimeField(default=now)
    blog_desciption = models.TextField(max_length=500)

    def __str__(self):
        return self.blog_title

