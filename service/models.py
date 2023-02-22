from django.db import models

# Create your models here.
class Image(models.Model):
    path = models.FileField(upload_to ='uploads/%Y/%m/%d/')
    alt = models.CharField(max_length=50,blank=True,default='')
    def __str__(self):
        return self.alt
    def delete(self,*args,**kwargs):#delete file from system also
        self.path.delete()
        super().delete(*args,**kwargs)


class ServiceType(models.Model):
    name = models.CharField(max_length=50,default='')
    slug = models.SlugField(max_length = 200,null=True)
    def __str__(self):
        return self.name


class Service(models.Model):
    service_type = models.ForeignKey(ServiceType,null=True,on_delete=models.CASCADE)
    name = models.CharField(max_length=50,default='')
    description = models.TextField(default='')
    images = models.ManyToManyField(Image,blank=True)
    def __str__(self):
        return self.name


class Reference(models.Model):
    service_type = models.ForeignKey(ServiceType,null=True,on_delete=models.CASCADE)
    name = models.CharField(max_length=50,default='')
    description = models.TextField(default='')
    images = models.ManyToManyField(Image,blank=True)
    def __str__(self):
        return self.name

class Expert(models.Model):
    image = models.ForeignKey(Image,null=True,on_delete=models.SET_NULL)
    title = models.CharField(max_length=50,default='')
    name = models.CharField(max_length=50,default='')
    description = models.TextField(default='')
    def __str__(self):
        return self.name
