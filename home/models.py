from os import truncate
from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.enums import Choices
from django.db.models.expressions import F
from django.db.models.fields.json import CaseInsensitiveMixin
from django.db.models.functions import Concat
from django.db.models import Max
from django.db.models.functions import Concat

import datetime
from datetime import datetime
from django.utils import timezone
# Create your models here.
class Destination:
    id: int
    name:str
    cls:int
    rno:int
    result:bool
class schoolmas(models.Model):
    udise=models.IntegerField()
    schoolcoe=models.IntegerField()
    Schoolnm=models.CharField(max_length=50)
    schooladdress=models.CharField( max_length=50,default=False, blank=False)
    def __str__(self):
        return self.Schoolnm
class statemas(models.Model):
   statenm=models.CharField(max_length=20, blank=False, default=False)
   def __str__(self):
       return self.statenm
class disttmas(models.Model):
    scode=models.ForeignKey(statemas,on_delete=CASCADE)
    #disttcd=models.CharField(max_length=2,blank=False,default=False)
    disttnm=models.CharField(max_length=25,blank=False,default=False)
    def __str__(self):
            return self.disttnm
class tehmas(models.Model):
    stcod=models.ForeignKey(statemas,on_delete=CASCADE)
    disttcd=models.ForeignKey(disttmas,on_delete=CASCADE)
   # tehcd=models.CharField(max_length=2,blank=False,default=False)
    tehname=models.CharField(max_length=25,default=False, blank=False)
    def __str__(self):
            return self.tehname
class pomas(models.Model):
    pincd=models.IntegerField()
    ponmame=models.CharField(max_length=20, default=False,blank=False)
    def __str__(self):
        return self.ponmame

class panchayatmas(models.Model):
    stcd=models.ForeignKey(statemas,on_delete=CASCADE)
    disttcd=models.ForeignKey(disttmas,on_delete=CASCADE)
    tehcd=models.ForeignKey(tehmas,on_delete=CASCADE)
    #pancd=models.CharField(max_length=2,default=False,blank=False)
    panname=models.CharField(max_length=20,default=False,blank=False)
    def __str__(self):
        return self.panname
class bankmas(models.Model):
    bankifsc=models.CharField(max_length=11, blank=False, default= False)
    bnkbranchnm=models.CharField(max_length=25,blank=False,default=False)
    def __str__(self):
        return self.bnkbranchnm
class classmas(models.Model):
    clasdesc=models.CharField(max_length=20, unique=True)
    classlvl=models.CharField(max_length=1,default=False,blank=False)
    def __str__(self):
        return self.clasdesc
class subjmas(models.Model):
    sujcname=models.CharField(max_length=30)
    def __str__(self):
        return self.sujcname



class desigmas(models.Model):
    empcatchoices = (('T', 'Teaching Staff'), ('N', 'Non Teaching Staff'),('S','SMC'))
    desigcd=models.AutoField(primary_key=True)
    deisgnm=models.CharField( max_length=50)
    desgcat=models.CharField(max_length=1,choices=empcatchoices,default='T')


    def __str__(self):
        return self.deisgnm

class  staffmas(models.Model):
   
    empsexchoices=(('M','Male'),('F','Feamle'),('O','Other/लागू नहीं'))
    empcstchoices = (('G','General'),('O','OBC'),('S','SC'),('T','ST'),('N','Not Applicable'))
    empid=models.AutoField(primary_key =True)
    schoolcd=models.ForeignKey(schoolmas,on_delete=CASCADE)
    empname=models.CharField(max_length=50, blank=False,null=False)
    pmiscode=models.IntegerField()
    empdob=models.DateField()
    empdoj=models.DateField()
    empquali=models.CharField(max_length=50)
    empmob=models.IntegerField()
    emppic=models.ImageField(upload_to ='staffpic')
    empemail=models.EmailField()
    sntyno=models.IntegerField()
    empsex=models.CharField(max_length=1,choices=empsexchoices,default='M')
    empcst=models.CharField(max_length=1,choices=empcstchoices,default='G')
    designation = models.ForeignKey(desigmas, on_delete=CASCADE)
    subject=models.ForeignKey(subjmas, on_delete=CASCADE,null=True,blank=True)    

    def __str__(self):
        return  self.empname
class studentbasic(models.Model):
     stcatchoices = (('G','General'),('O','OBC'),('S','SC'),('T','ST'),('N','Not Applicable'))
     stsexchoices = (('M','Male'),('F','Feamle'),('O','Other'))
     streligionchoices = (('H','Hindu'),('M','Muslim'),('S','Sikh'),('C','Christian'))
     #strealtionchoices = (('S','S/O पुत्र'),('D','D/O पुत्री '))
     stdname=models.CharField(max_length=25,blank=False,default=False)
     #strltion=models.CharField(max_length=1,choices=strealtionchoices,default='S')
     stfname=models.CharField(max_length=25,blank=False,default=False)
     stmname=models.CharField(max_length=25,blank=False,default=False)
     strelig=models.CharField(max_length=1,choices=streligionchoices,default='H')
     stcat=models.CharField(max_length=1,choices=stcatchoices,default='G')
     stsex=models.CharField(max_length=1,choices=stsexchoices,default='M')
     stdob=models.DateField()
     stdoa=models.DateField()
     stclass=models.ForeignKey(classmas,on_delete=CASCADE)
     Stadmno=models.IntegerField()
     stadyear=models.IntegerField()
     stdacct=models.IntegerField()
     stbank=models.ForeignKey(bankmas,on_delete=CASCADE)
     stdmob=models.IntegerField()
     stduid=models.IntegerField()
     stvillg=models.CharField(max_length=25,blank=False,default=False)
     stdistt=models.ForeignKey(disttmas,on_delete=CASCADE)
     Stteh=models.ForeignKey(tehmas,on_delete=CASCADE)
     stpo=models.ForeignKey(pomas,on_delete=CASCADE)
     stpanch=models.ForeignKey(panchayatmas,on_delete=CASCADE)
     stsatus=models.CharField(max_length=1,default=False,blank=False)
     def __str__(self):
        return self.stdname,self.stclass








