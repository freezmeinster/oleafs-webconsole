from django.contrib import admin
from cloud import models

admin.site.register(models.AddHarddisk)
admin.site.register(models.AddNetwork)
admin.site.register(models.Cloud)
admin.site.register(models.CloudLog)
admin.site.register(models.Node)
admin.site.register(models.NodeLog)
admin.site.register(models.OS)
admin.site.register(models.Template)