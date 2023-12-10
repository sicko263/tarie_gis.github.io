from django.contrib.gis.db import models

# Create your models here.
class Myfarms(models.Model):
    gid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=40, blank=True, null=True)
    province = models.CharField(max_length=40, blank=True, null=True)
    district = models.CharField(max_length=40, blank=True, null=True)
    status = models.CharField(max_length=25, blank=True, null=True)
    area_ha = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    area_acre = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    class_field = models.CharField(db_column='class', max_length=100, blank=True, null=True)  # Field renamed because it was a Python reserved word.
    maize = models.FloatField(blank=True, null=True)
    fertilizer = models.FloatField(blank=True, null=True)
    sorghum = models.FloatField(blank=True, null=True)
    geom = models.MultiPolygonField(srid=0, blank=True, null=True)


    def __str__(self):
        return str(self.name) + " " +":"+ " "+ str (self.province)
    
    class Meta:
        managed = False
        db_table = 'myfarms'



class provinces(models.Model):
    name = models.CharField(max_length=1000, null=True, blank=True)

    def __str__(self):
        return str(self.name)
    
    class Meta:
        ordering = ('name', )


class province_allocation(models.Model):
    province            = models.ForeignKey(provinces, on_delete=models.CASCADE, null=True, blank=True)
    maize               = models.DecimalField(max_digits=100, decimal_places=2, null=True, blank=True)
    fertilizer          = models.DecimalField(max_digits=100, decimal_places=2, null=True, blank=True)
    sorghum             = models.DecimalField(max_digits=100, decimal_places=2, null=True, blank=True)
    date_created        = models.DateTimeField('date created',  auto_now_add=True, null=True)
    date_updated        = models.DateTimeField('date updated', auto_now=True, null=True)


    def __str__(self):
        return str(self.province)
    
    class Meta:
        ordering = ('date_created', )






class Newfarms(models.Model):
    gid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=40, blank=True, null=True)
    province = models.CharField(max_length=40, blank=True, null=True)
    district = models.CharField(max_length=40, blank=True, null=True)
    area_ha = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    area_acre = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    class_field = models.CharField(db_column='class', max_length=100, blank=True, null=True)  # Field renamed because it was a Python reserved word.
    maize = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    fertilizer = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    sorghum = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    status = models.CharField(max_length=15, blank=True, null=True)
    geom = models.MultiPolygonField(srid=0, blank=True, null=True)


    def __str__(self):
        return str(self.name) + " " +":"+ " "+ str (self.province)
    

    class Meta:
        managed = False
        db_table = 'newfarms'


class farms_allocation(models.Model):
    farms               = models.ForeignKey(Newfarms, on_delete=models.CASCADE, null=True, blank=True)
    maize               = models.DecimalField(max_digits=100, decimal_places=2, null=True, blank=True)
    fertilizer          = models.DecimalField(max_digits=100, decimal_places=2, null=True, blank=True)
    sorghum             = models.DecimalField(max_digits=100, decimal_places=2, null=True, blank=True)
    date_created        = models.DateTimeField('date created',  auto_now_add=True, null=True)
    date_updated        = models.DateTimeField('date updated', auto_now=True, null=True)


    def __str__(self):
        return str(self.maize)
    
    class Meta:
        ordering = ('date_created', )

