from django.db import models
from support.models import CloudUser

class Node(models.Model):
    hypervisor = (
        ("kvm","KVM -- Full Virtualization"),
        ("kvm","Xen -- Paravirtualization"),
    )
    name = models.CharField(max_length=255)
    total_mem = models.IntegerField()
    total_hdd = models.IntegerField()
    ip_address = models.IPAddressField()
    hypervisor = models.CharField(max_length=4,choices=hypervisor)
    is_active = models.BooleanField()
    
    def __unicode__(self):
        return self.name

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
    name = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    base_size = models.IntegerField()
    format_storage = models.CharField(max_length=20,choices=format)
    path = models.CharField(max_length=255)
    is_active = models.BooleanField()

class Template(models.Model):
    name = models.CharField(max_length=255)
    asign_mem = models.IntegerField()
    asign_hdd = models.IntegerField()
    is_active = models.BooleanField()

class Cloud(models.Model):
    name = models.CharField(max_length=255)
    mac_address = models.CharField(max_length=20)
    ip_address = models.IPAddressField()
    node = models.ForeignKey(Node)
    template = models.ForeignKey(Template)
    os = models.ForeignKey(OS)
    user = models.ForeignKey(CloudUser)
    is_active = models.BooleanField()

class CloudLog(models.Model):
    cloud = models.ForeignKey(Cloud)
    free_mem = models.IntegerField()
    free_hdd = models.IntegerField()
    proc = models.IntegerField()
    periode = models.DateTimeField(auto_now_add=True)

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
    is_active = models.BooleanField()

class AddNetwork(models.Model):
    cloud = models.ForeignKey(Cloud)
    mac_address = models.CharField(max_length=20)
    ip_address = models.IPAddressField()
    is_active = models.BooleanField()



