from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=255)
    introduction = models.TextField(null=True)
    body_list = models.TextField(null=True)
    conclusion = models.TextField(null=True)
    created_date = models.DateField(auto_now_add=True, null=True)
    updated_date = models.DateField(auto_now=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        db_table = 'blog'
        verbose_name_plural = 'blog'
        ordering = ['created_date']
