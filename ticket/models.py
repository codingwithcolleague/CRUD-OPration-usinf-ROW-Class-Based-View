from django.db import models

# Create your models here.

STATUS_CHOICES = (
    ('inprocess','In Process'),
    ('completed', 'Completed'),
    ('notstarted', 'Not Started')

)

class Metro(models.Model):
    name = models.CharField(max_length=200 , blank=True,null=True)
    mobile = models.CharField(max_length=200 , blank=True,null=True)
    startplace = models.CharField(max_length=200 , blank=True,null=True)
    endplace = models.CharField(max_length=200 , blank=True,null=True)
    status = models.CharField(max_length=10,choices=STATUS_CHOICES , default='notstarted')
    
    def __str__(self):
        return self.name +  "--"  + self.startplace +  "--"  + self.endplace
    
    