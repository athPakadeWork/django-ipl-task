from django.db import models

class School(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    mgmt = models.CharField(max_length=50)
    moi = models.CharField(max_length=50,blank=True, null=True)
    cat = models.CharField(max_length=50)
    sex = models.CharField(max_length=20)
    cluster_name = models.CharField(max_length=255,blank=True, null=True)
    block_name = models.CharField(max_length=255,blank=True, null=True)
    district_name = models.CharField(max_length=255)
    school_type = models.CharField(max_length=50)
    assembly_name = models.CharField(max_length=255, blank=True, null=True)
    parliament_name = models.CharField(max_length=255, blank=True, null=True)
    pincode = models.CharField(max_length=20, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    landmark = models.CharField(max_length=255, blank=True, null=True)
    bus = models.CharField(max_length=255, blank=True, null=True)
    coord = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"{self.name} ({self.school_type} - {self.district_name})"
