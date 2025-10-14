

from django.contrib import admin



from myapp.models import Curiosity, Comment
from users.models import Profile

# Register your models here.
admin.site.register(Curiosity)
admin.site.register(Profile)
admin.site.register(Comment)