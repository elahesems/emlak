from django.db import models

# Create your models here.

class Sliders(models.Model):
    image=models.ImageField(null=True, blank=True)
    title=models.CharField(max_length=45)
    description=models.CharField(max_length=700)

    def __str__(self):
        return self.title

    def delete(self,*args,**kwargs):
        self.image.delete()
        super().delete(*args,**kwargs)


class Homes(models.Model):
    units=(
        ('tl','₺'),
        ('euro','€'),
        ('dollar','$')

    )
    type_of=(
        ('kiralik','kiralık'),
        ('satlik','satlık')
    )
    name=models.CharField(max_length=150, verbose_name='Home name')
    price=models.CharField(max_length=150)
    price_unit=models.CharField(max_length=150,choices=units,default='tl')
    bathrooms=models.CharField(max_length=150)
    square=models.CharField(max_length=150)
    parking=models.CharField(max_length=150)
    rooms=models.CharField(max_length=150)
    image = models.ImageField(null=True, blank=True)
    address=models.CharField(max_length=150,null=True,blank=True)
    type=models.CharField(max_length=150,choices=type_of,default='kiralik')
    #status = models.BooleanField(default=True,verbose_name='gosterilsin mi?')




    def __str__(self):
        return self.name



class Customer(models.Model):
    name=models.CharField(max_length=50)
    phone=models.CharField(max_length=50)
    email=models.CharField(max_length=50,null=True,blank=True)
    message=models.TextField(null=True,blank=True)
    selected_home=models.ForeignKey(Homes,null=True,on_delete=models.CASCADE)

    def __str__(self):
        return self.name


