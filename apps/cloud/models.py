from django.db import models
from support.models import CloudUser
from django.template.defaultfilters import safe

class Node(models.Model):
    hypervisor = (
        ("kvm","KVM -- Full Virtualization"),
        ("xen","Xen -- Paravirtualization"),
    )
    ARC = (
        ('x86_64','64 Bit'),
        ('i386','32 Bit'),
    )
    name = models.CharField(max_length=255)
    total_mem = models.IntegerField(verbose_name="Total Memory (MB)")
    total_hdd = models.IntegerField(verbose_name="Total Harddisk (GB)")
    architecture = models.CharField(max_length=4,choices=ARC)
    ip_address = models.IPAddressField()
    hypervisor = models.CharField(max_length=4,choices=hypervisor)
    is_active = models.BooleanField(default=True)
    
    def __unicode__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Data Node"

class NodeLog(models.Model):
    node = models.ForeignKey(Node)
    free_mem = models.IntegerField()
    free_hdd = models.IntegerField()
    periode = models.DateTimeField(auto_now_add=True)

class OS(models.Model):
    format = (
        ("qcow","QCOW"),
        ("raw","RAW"),
        ("qcow2","QCOW 2"),
        ("vdi","VDI"),
    )
    ARC = (
        ('x86_64','64 Bit'),
        ('i386','32 Bit'),
    )
    name = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    architecture = models.CharField(max_length=4,choices=ARC)
    base_size = models.IntegerField(verbose_name="Base Storage (GB)")
    format_storage = models.CharField(max_length=20,choices=format)
    path = models.CharField(max_length=255)
    logo = models.ImageField(upload_to="os")
    is_active = models.BooleanField(default=True)
    
    def logo_img(self):
        return safe("<img hight='84px' src=/static/user/%s>" % self.logo.url )
    
    
    def __unicode__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Data Sistem Operasi"
    

class Template(models.Model):
    name = models.CharField(max_length=255)
    asign_mem = models.IntegerField(verbose_name="Asigned Memory (MB)")
    asign_hdd = models.IntegerField(verbose_name="Asigned Harddisk (GB)")
    is_active = models.BooleanField(default=True)
    
    class Meta:
        verbose_name_plural = "Data Template"
    
    def __unicode__(self):
        return self.name
    

class Cloud(models.Model):
    STATE = (
        ('run','Running'),
        ('stop','Stopped')
    )
    
    name = models.CharField(max_length=255)
    mac_address = models.CharField(max_length=20)
    ip_address = models.IPAddressField()
    node = models.ForeignKey(Node)
    domain_name = models.CharField(max_length=255)
    template = models.ForeignKey(Template)
    os = models.ForeignKey(OS)
    user = models.ForeignKey(CloudUser)
    vnc_port = models.IntegerField()
    websocket_port = models.IntegerField()
    is_created = models.BooleanField()
    run_state = models.CharField(max_length=255,choices=STATE)
    is_active = models.BooleanField()
    
    class Meta:
        verbose_name_plural = "Data Cloud"
        unique_together = ['mac_address','ip_address']
        
    def __unicode__(self):
        return self.name
    
class CloudLog(models.Model):
    cloud = models.ForeignKey(Cloud)
    free_mem = models.IntegerField()
    free_hdd = models.IntegerField()
    proc = models.IntegerField()
    periode = models.DateTimeField(auto_now_add=True)
    
    def __unicode__(self):
        return self.cloud.name

class CloudRunLog(models.Model):
    STATE = (
        ('run','Running'),
        ('stop','Stopped')
    )
    cloud = models.ForeignKey(Cloud)
    periode = models.DateTimeField(auto_now_add=True)
    run_state = models.CharField(max_length=255,choices=STATE)
    message = models.TextField()
    
    def __unicode__(self):
        return self.cloud.name
    
class AddHarddisk(models.Model):
    format = (
        ("qcow","QCOW"),
        ("raw","RAW"),
        ("qcow2","QCOW 2"),
        ("vdi","VDI"),
    )
    cloud = models.ForeignKey(Cloud)
    size = models.IntegerField()
    format_storage = models.CharField(max_length=20,choices=format)
    path = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    
    class Meta:
        verbose_name_plural = "Data Harddisk tambahan"

class AddNetwork(models.Model):
    cloud = models.ForeignKey(Cloud)
    mac_address = models.CharField(max_length=20)
    ip_address = models.IPAddressField()
    is_active = models.BooleanField()
    
    class Meta:
        verbose_name_plural = "Data Network Interface"



