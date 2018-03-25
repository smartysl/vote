from django.contrib import admin
from .models import question,answer,User
admin.site.register(question)
admin.site.register(answer)
admin.site.register(User)
# Register your models here.
