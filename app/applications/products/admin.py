from django.contrib import admin

from applications.products import models

admin.site.register(models.Product)
admin.site.register(models.Category)
admin.site.register(models.Tag)
