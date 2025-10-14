from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.urls import reverse

from mywebsite import settings


class Curiosity(models.Model):
    topic = models.CharField(max_length=50)
    content = models.TextField()
    stupidity_scale = models.IntegerField(
        validators=[
            MinValueValidator(0),
            MaxValueValidator(100)
        ]
    )
    user_name = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, default=1)
    picture = models.CharField(max_length=500, default="https://animalclinic.org/wp-content/uploads/2019/05/paw-placeholder.png")

    def __str__(self):
        return self.topic

    def get_absolute_url(self):
        return reverse('myapp:index')



class Comment(models.Model):
    curiosity = models.ForeignKey(Curiosity, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(max_length=500)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('created_on',)

    def __str__(self):
        return self.content