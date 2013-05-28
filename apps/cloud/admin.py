from django.contrib import admin
from cloud import models

class OsAdmin(admin.ModelAdmin):
    list_display = ('name','logo_img','architecture','base_size','password','format_storage','path','is_active')
    search_fields = list_display
    list_filter = ('is_active','format_storage','architecture')
    
class NodeAdmin(admin.ModelAdmin):
    list_display = ('name','hypervisor','architecture','ip_address','total_mem','total_hdd','is_active')
    search_fields = list_display
    list_filter = ('is_active','hypervisor','architecture')
    
class CloudAdmin(admin.ModelAdmin):
    list_display = ['name','mac_address','ip_address','node','os','template','user','vnc_port','websocket_port','is_created','run_state']
    search_fields = list_display
    list_filter = ['node','os','template','is_created','run_state']
class TemplateAdmin(admin.ModelAdmin):
    list_display = ['name','asign_mem','asign_hdd','is_active']
    
class AddHddAdmin(admin.ModelAdmin):
    list_display = ['cloud',]

class AddNetAdmin(admin.ModelAdmin):
    list_display = ['cloud',]
    
admin.site.register(models.AddHarddisk,AddHddAdmin)
admin.site.register(models.AddNetwork,AddNetAdmin)
admin.site.register(models.Cloud,CloudAdmin)
admin.site.register(models.CloudLog)
admin.site.register(models.CloudRunLog)
admin.site.register(models.Node,NodeAdmin)
admin.site.register(models.NodeLog)
admin.site.register(models.OS,OsAdmin)
admin.site.register(models.Template, TemplateAdmin)