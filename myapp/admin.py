

from django.contrib import admin
from django.contrib.auth.models import User

from myapp.models import Curiosity
from users.models import Profile

# Register your models here.
admin.site.register(Curiosity)
admin.site.register(Profile)