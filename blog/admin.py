from django.contrib import admin
from blog import models
# Register your models here.


admin.site.register(models.Tag)

class PostAdmin(admin.ModelAdmin):
  prepopulated_fields={"slug":("title",)}

admin.site.register(models.Post,PostAdmin)