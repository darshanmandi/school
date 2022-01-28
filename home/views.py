from django.db.models.functions.text import PostgreSQLSHAMixin
from django.shortcuts import render
from django.http import  HttpResponse, request
from Hello.settings import BASE_DIR
from pathlib import Path,os
from django.db import models
from django.db.models import manager,functions

from home.models import desigmas, disttmas, panchayatmas, schoolmas, staffmas,Destination, statemas, subjmas, tehmas


# Create your views here.
def index(request):

    context={
        'darshan':'This is Sent Darshan !'
    }
    return render(request,'index.html',context)
def about(request):
    return render(request,'about.html')
   # return HttpResponse("This is about page")
def contact(request):
    return render(request,'contact.html')
    #return HttpResponse("this is contact")
def service(request):
    return render(request,'service.html')
        #return HttpResponse("this is service")
def add(request):
    #val1 =int(request.POST['num1'])
    #val2 =int(request.POST['num2'])
    #res=val1 + val2

    dss1= Destination()
    dss1.name= request.POST['name'] 
    dss1.cls=request.POST['cls']
    dss1.rno=request.POST['rno']
    dss1.result=request.POST['result']


    return render(request,'result.html',{'dss1':dss1})
def staffadd(request, catr):
    
  
    empsexchoices = (('M','Male'),('F','Feamle'),('O','Other/लागू नहीं'))
    empcstchoices = (('G','General'),('O','OBC'),('S','SC'),('T','ST'),('N','Not Applicable'))
    desglist=desigmas.objects.filter(desgcat=catr)
    if catr == 'T':
        subjlist=subjmas.objects.all()
    else:
        subjlist = subjmas.objects.filter(id = 11)
    catlist=desigmas.objects.filter(desgcat=catr)

    submitted = False         
    
    if request.method == 'POST':
        print(request.POST)
        scd='3003'
        scr = schoolmas.objects.get(schoolcoe = scd)
        empnm=request.POST['emp']
        desg=request.POST['desg']
        desr = desigmas.objects.get(desigcd = desg)
        gend=request.POST['gend']
        
        subj=request.POST['subj']
     
        subr = subjmas.objects.get(id = subj)
        ecat=request.POST['ecat']
        dob=request.POST['dob']
        doj=request.POST['doj']
        pmis=request.POST['pmis']
        mob=request.POST['mob']
        qua=request.POST['qua']
        seno=request.POST['seno']
        email=request.POST['email']
        epic=request.FILES['pic']
        newemp = staffmas(schoolcd = scr, empname = empnm, pmiscode = pmis, empdob = dob, empdoj = doj,empquali=qua,empmob=mob,emppic=epic,empemail=email,sntyno=seno,empsex=gend,empcst=ecat,designation=desr,subject=subr )
        newemp.save()
        submitted = True
    context =    {
        'desglist': desglist,
        'subjlist'  : subjlist,
        'cstlist'   : empcstchoices,
        'sex'       : empsexchoices,
        'catlist'   : catlist,
        'submitted' : submitted,
        'catr'      :catr
    }
    return render(request,'staffadd.html', context)
def Staff(request, cat):
    cattype=desigmas.objects.filter(desgcat=cat)
    

    staff=staffmas.objects.filter(designation__desgcat=cat)
    context = {
        'cattype':cattype,
        'staff':staff,
        'cat':cat
    }
    #bdir=os.path.join(BASE_DIR,'staffpic')
    return render(request,'Staff.html',context)
    # return render(request,'Staff.html',context,{'staff':staff, 'bdir' : bdir})
def mentry(request):
    sttnm=statemas.objects.all()
    distl=disttmas.objects.filter(scode = sttnm.id)
    context= {
        'sttnm': sttnm,
        'distl': distl
    }
    return render (request,'masterentry.html',context)

def addedittehsil(request):
    discd = 0
    
    stcd = 1
    
    strec = statemas.objects.get(id = stcd)
    dislist = disttmas.objects.filter(scode=strec)
    if request.method == 'POST':
        print(request.POST)
        if 'back' in request.POST:
            pass
        elif 'dis' in request.POST:
            discd = int(request.POST['dis'])
            disr = disttmas.objects.get(id = discd)
            tehlist = tehmas.objects.filter(stcod = strec, disttcd = disr)
            disnm = disr.disttnm
            tehselected = False
            context = {
                'discd' : discd,
                'disnm' : disnm,
                'tehlist' : tehlist,
                'tehselected' : tehselected

            }
            return render (request, 'addedittehsil.html', context)
        elif 'edit' in request.POST:
            tehcd = int(request.POST['edit'])
            tehrec = tehmas.objects.get(id = tehcd)
            discd = int(request.POST['discd'])
            context = {
                'discd' : discd,
                'tehcd' : tehrec.id,
                'tehnm' : tehrec.tehname,
                'tehselected' : True

            }
            return render (request, 'addedittehsil.html', context)
        elif 'addmore' in request.POST:
            tehcd = 0
            #tehrec = tehmas.objects.get(id = tehcd)
            discd = int(request.POST['discd'])
            context = {
                'discd' : discd,
                'tehcd' : tehcd,
                'tehnm' : '',
                'tehselected' : True

            }
            return render (request, 'addedittehsil.html', context)
        elif 'save' in request.POST:
            tehcd = int(request.POST['tehcd'])
            discd = int(request.POST['discd'])
            tehname = request.POST['aname']
            disr = disttmas.objects.get(id = discd)
            if tehcd == 0:
                tehrec = tehmas(stcod=strec,disttcd=disr,tehname=tehname)
            else:
                tehrec = tehmas.objects.get(id = tehcd)
                tehrec.tehname = tehname

            tehrec.save()
            context = {
                'discd' : discd,
                'disnm' : disr.disttnm,
                'tehlist' : tehmas.objects.filter(stcod = strec, disttcd = disr),
                'tehselected' : False

            }
            return render (request, 'addedittehsil.html', context)


    context = {
        'discd' : discd,
        'dislist' : dislist
    }
    return render (request, 'addedittehsil.html', context)
def addeditpanchyat(request):
    discd = 0
    tehcd = 0
    stcd = 1
    strec=statemas.objects.get(id=stcd)
    dislist=disttmas.objects.filter(scode=strec)
    tehlist= None
    if request.method=='POST':
        print(request.POST)
        if 'dis' in request.POST and 'teh' not in request.POST:
            discd=int(request.POST['dis'])
            disrec= disttmas.objects.get(id = discd)
            tehlist=tehmas.objects.filter(stcod = strec, disttcd = disrec)
            disnm = disrec.disttnm
            tehselected = False
            context = {
                'discd' : discd,
                'disnm' : disnm,
                'dislist'   :   dislist,                
                'tehlist' : tehlist,
                'tehselected' : tehselected,
                'tehcd'        :tehcd

            }
            return render(request,'addeditpanchayt.html',context)
        elif 'teh' in (request.POST):
            tehcd=int(request.POST['teh'])
            tehrec=tehmas.objects.get(id=tehcd)
            discd=int(request.POST['discd'])
            disrec=disttmas.objects.get(id=discd)
            panlist= panchayatmas.objects.filter(stcd=strec,tehcd=tehrec,disttcd=disrec)
            disnm=disrec.disttnm
            tehnm=tehrec.tehname
            panselected=False
            context ={
                'discd':discd,
                'disnm' : disnm,
                'tehcd' : tehcd,
                'tehnm' : tehnm,
                'panlist':panlist,
                'panselected':panselected
            }
            return render(request,'addeditpanchayt.html',context)
        elif 'edit' in request.POST:
            pancd = int(request.POST['edit'])
            panrec = panchayatmas.objects.get(id = pancd)
            discd = int(request.POST['discd'])
            tehcd= int(request.POST['tehcd'])
            context = {
                'discd' : discd,
                'tehcd' : tehcd,
                'pancd' :panrec.id,
                'panname' :panrec.panname,
                'panselected' : True

            }
            return render (request, 'addeditpanchayt.html', context)
        
        elif 'addmore' in request.POST:
            pancd = 0
            #tehrec = tehmas.objects.get(id = tehcd)
            discd = int(request.POST['discd'])
            tehcd=int(request.POST['tehcd'])
            context = {
                'discd' : discd,
                'tehcd' : tehcd,
                'pancd' : pancd,
                'panname' : '',
                'panselected' : True

            }
            return render (request, 'addeditpanchayt.html', context)
        elif 'save' in request.POST:
            tehcd = int(request.POST['tehcd'])
            discd = int(request.POST['discd'])
            pancd=int(request.POST['pancd'])
            panname = request.POST['aname']
            disrec=disttmas.objects.get(id=discd)
            tehrec=tehmas.objects.get(id=tehcd)
            if pancd == 0:
                panrec = panchayatmas(stcd=strec,disttcd=disrec,tehcd=tehrec,panname=panname)
            else:
                panrec = panchayatmas.objects.get(id = pancd)
                panrec.panname = panname

            panrec.save()
            context = {
                'discd' : discd,
                'disnm' : disrec.disttnm,
                'tehcd' : tehcd,
                'tehnm' : tehrec.tehname,
                'panlist' : panchayatmas.objects.filter(stcd = strec, disttcd = disrec,tehcd=tehrec),
                'panselected' : False

            }
            return render(request,'addeditpanchayt.html',context)

    context = {
        'discd'     :    discd,
        'dislist'   :   dislist,
        'tehcd'     : tehcd,
        'tehlist'   : tehlist

    }
    return render(request,'addeditpanchayt.html',context)

# District Add Edit View
def addeditdistt(request):
    stcd=1
    strec=statemas.objects.get(id=stcd)
    dislist=disttmas.objects.filter(scode=strec)
    disttselected=False
    if request.method == 'POST':
        print(request.POST)
        if 'back' in request.POST:
            pass
        elif 'edit' in request.POST:
            discd=int(request.POST['dis'])
            print(request.POST)
            disrec=disttmas.objects.get(scode=strec,disttcd=discd)
            context ={
                'discd':disrec.id,
                'disname':  disrec.disttnm,
                'stnm'  :strec.statenm,
                'disttselected':True
            }
            return render (request,'adddistt.html',context)
        elif 'addmore' in request.POST:
            discd = 0
            #tehrec = tehmas.objects.get(id = tehcd)
           
            context = {
                'discd' : discd,
                
                'disstselected' : True

            }
        elif 'save' in request.POST:
            discd=int(request.POST['disttcd'])
            disnm=request.POST['aname']
            if discd == 0 :
                disrec=disttmas(scode=strec,disttnm=disnm)
            else:
                disrec=disttmas.objects.get(id=discd)
                disrec.disttnm=disnm
            disrec.save()
            context ={
                'stnm': strec.statenm,
                'dislist':disttmas.objects.filter(socde=strec.id),
                'disttselected':False
            }

            return render(request,'adddistt.html',context)
    
    context ={
        'stcd':stcd,
        'dislist': dislist
            }
    return render(request,'adddistt.html',context)

