from django.db.models.functions.text import PostgreSQLSHAMixin
from django.shortcuts import render
from django.http import  HttpResponse, request
from pkg_resources import PkgResourcesDeprecationWarning
from Hello.settings import BASE_DIR
from pathlib import Path,os
from django.db import models
from django.db.models import manager,functions

from home.models import bankmas, classmas, classsubject, desigmas, disttmas, panchayatmas, pomas, schoolmas, staffmas,Destination, statemas, subjmas, tehmas


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
    stnm=strec.statenm
    dislist=disttmas.objects.filter(scode=strec)
    disttselected=False
    if request.method == 'POST':
        print(request.POST)
        if 'back' in request.POST:
            pass
        elif 'edit' in request.POST:
            discd=int(request.POST['edit'])
            print(request.POST)
            disrec=disttmas.objects.get(scode=strec,id=discd)
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
                'disname':'',
                'disttselected' : True

            }
            return render (request,'adddistt.html',context)
        elif 'save' in request.POST:
            discd=int(request.POST['dis'])
            disnm=request.POST['aname']
            if discd == 0 :
                disrec=disttmas(scode=strec,disttnm=disnm)
            else:
                disrec=disttmas.objects.get(id=discd)
                disrec.disttnm=disnm
            disrec.save()
            context ={
                'stnm': strec.statenm,
                'dislist':disttmas.objects.filter(scode=strec.id),
                'disttselected':False
            }

            return render(request,'adddistt.html',context)
    
    context ={
        'stcd':stcd,
        'dislist': dislist,
        'disttselected':disttselected,
        'stnm':stnm
            }
    return render(request,'adddistt.html',context)

def addeditsubject(request):
    subselect = False,
    sublist = subjmas.objects.all()
    if request.method == 'POST':
        print(request.POST)
        if 'back' in request.POST:
            pass
        elif 'edit' in request.POST:
            subcd=int(request.POST['edit'])
            print(request.POST)
            subrec=subjmas.objects.get(id=subcd)
            context ={
                'subcd':subrec.id,
                'subname':  subrec.sujcname,
                'subselect':True
            }
            return render (request,"addeditsubject.html",context)
        elif 'addmore' in request.POST:
            subcd=0
            context ={
                'subcd': subcd,
                'subname':'',
                'subselect':True
            }
            return render(request,"addeditsubject.html",context)
        elif 'save' in request.POST:
            subcd=int(request.POST['subcd'])
            subnm=request.POST['subname']
            if subcd==0 :
                subrec=subjmas(sujcname=subnm)
            else:
                subrec=subjmas.objects.get(id=subcd)
                subrec.sujcname=subnm
            subrec.save()
            context ={
                'sublist':subjmas.objects.all(),
                'subselect': False
            }

            return render(request,"addeditsubject.html",context)
    context={
        'sublist':sublist,
        'subselect':False
    }
    return render(request,"addeditsubject.html",context)
def addeditbank(request):
    banklist=bankmas.objects.all()
    if request.method == 'POST':
        print(request.POST)
        if 'back' in request.POST:
            pass
        elif 'addmore' in request.POST:
            bankcd=0
            context ={
                'bankcd':bankcd,
                'bnkname':'',
                'ifsc':'',
                'bankselect':True

            }
            return render(request,"addeditbnkbrnch.html",context)
        elif 'edit' in request.POST:
            bankcd=int(request.POST['edit'])
            bankrec=bankmas.objects.get(id=bankcd)
            context ={
                'bnkname':bankrec.bnkbranchnm,
                'ifsc':bankrec.bankifsc,
                'bankcd':bankrec.id,
                'bankselect':True
            }
            return render(request,"addeditbnkbrnch.html",context)

        elif 'save' in request.POST:
            bankcd=int(request.POST['bankcd'])
            bnkname=request.POST['bnkname']
            ifsc=request.POST['ifsc']
            if bankcd==0:
                bankrec=bankmas(bankifsc=ifsc,bnkbranchnm=bnkname)
            else:
                bankrec=bankmas.objects.get(id=bankcd)
                bankrec.bnkbranchnm=bnkname
                bankrec.bankifsc=ifsc
            bankrec.save()
            context={
                'bankselect':False,
                'banklist':bankmas.objects.all()
            }
            return render(request,"addeditbnkbrnch.html",context)


    context ={
        'banklist':banklist,
        'bankselect': False
    }
    return render(request,"addeditbnkbrnch.html",context)
def addeditpo(request):
    stcd=1
    discd=0
    dislist=disttmas.objects.filter(scode=stcd)
    if request.method=='POST':
        print(request.POST)
        if 'back' in request.POST:
            pass
        elif 'dis' in request.POST:
            discd=int(request.POST['dis'])
            disrec=disttmas.objects.get(id=discd)
            polist=pomas.objects.filter(distcd=discd)
            context ={
                'polist':polist,
                'discd':disrec.id,
                'disnm':disrec.disttnm,
                'poselected':False
            }
            return render(request,"addeditpo.html",context)
        elif 'addmore' in request.POST:
            discd=int(request.POST['discd'])
            disrec=disttmas.objects.get(id=discd)
            pocd=0
            context ={
                'discd':disrec.id,
                'disnm':disrec.disttnm,
                'pocd':pocd,
                'poname':'',
                'pincd':'',
                'poselected':True
            }
            return render(request,"addeditpo.html",context)
        elif 'edit' in request.POST:
            discd=int(request.POST['discd'])
            pocd=int(request.POST['edit'])
            disrec=disttmas.objects.get(id=discd)
            prec=pomas.objects.get(id=pocd)
            context={
                'pocd':pocd,
                'poname':prec.ponmame,
                'pin'   :prec.pincd,
                'discd': disrec.id,
                'disnm':disrec.disttnm,
                'poselected':True
            }
            return render(request,"addeditpo.html",context)
        elif 'save' in request.POST:
            discd=int(request.POST['discd'])
            disrec=disttmas.objects.get(id=discd)
            pocd=int(request.POST['pocd'])
            pin=int(request.POST['pin'])
            poname=request.POST['poname']
            if pocd == 0:
                prec=pomas(pincd=pin,ponmame=poname,distcd=disrec)
            else:
                prec=pomas.objects.get(id=pocd)
                prec.pincd=pin
                prec.ponmame=poname
            prec.save()
            context ={
                'discd':discd,
                'disnm':disrec.disttnm,
                'polist':pomas.objects.all(),
                'poselected':False
            }
            return render(request,"addeditpo.html",context)

            

    context ={
        'dislist':dislist,
        'discd': discd,
        'disselect': False
    }
    return render(request,"addeditpo.html",context)
def addeditstate(request):
    stlist=statemas.objects.all()
    stselect=False
    if request.method=='POST':
        print(request.POST)

        if 'back' in request.POST:
            pass
        elif 'addmore' in request.POST:
            stcd=0
            context ={
                'stcd':stcd,
                'stname':'',
                'stselect':True
            }
            return render(request,"addeditstate.html",context)
        elif 'edit' in request.POST:
            stcd=int(request.POST['edit'])
            strec=statemas.objects.get(id=stcd)
            context ={
                'stcd':strec.id,
                'stname':strec.statenm,
                'stselect': True
            }
            return render(request,"addeditstate.html",context)
        elif 'save' in request.POST:
            stcd=int(request.POST['stcd'])
            stnm=request.POST['stname']
            
            if stcd == 0:
                strec=statemas(statenm=stnm)
            else:
                strec=statemas.objects.get(id=stcd)
                strec.statenm=stnm
            strec.save()
            context ={
            'stlist':statemas.objects.all(),
            'stselect':False
            }
            return render(request,"addeditstate.html",context)
        


    context={
        'stlist':stlist,
        'stselect':stselect

    }

    return render(request,"addeditstate.html",context)

def subjmapp(request):
    clcd = 0
    maplist=classsubject.objects.filter(clscd=clcd).order_by ('clscd')
    cllist= classmas.objects.all()
    subjlist=subjmas.objects.all()
    if request.method=='POST':
        print(request.POST)
        if 'back' in request.POST:
            pass
        elif 'cls' in request.POST:
            clcd=int(request.POST['cls'])
            clrec=classmas.objects.get(id=clcd)
            maplist=classsubject.objects.filter(clscd=clrec.id)
            context={
                 'cllist':cllist,
                 'maplist':maplist,
                'clcd':clcd,
                'mpadd':False
            }
            return render(request,'classsubject.html',context)
        elif 'addmore' in request.POST:
            mpid=0
            subj=subjmas.objects.all()
            clcd=int(request.POST['clscd'])
            clas=classmas.objects.get(id=clcd)
            context={
                'clas':clas.id,
                'clasnm':clas.clasdesc,
                'subjlist':subj,
                'subid':None,
                'tmark':'',
                'amark':'',
                'pmark':'',
                'comb':'',
                'mpid':mpid,
                 'mpadd':True
            }
            return render(request,'classsubject.html',context)
        elif 'edit' in request.POST:
            mpid=int(request.POST['edit'])
            mprec=classsubject.objects.get(id=mpid)
            clas=classmas.objects.get(clasdesc=mprec.clscd)
            subj=subjmas.objects.get(sujcname=mprec.subj)
            context ={
            'mpid':mpid,
            'clas':clas.id,
            'clasnm':mprec.clscd.clasdesc,
            'subid':subj.id,
            'tmark':mprec.tmm,
            'amark':mprec.amm,
            'pmark':mprec.pmm,
            'comb':mprec.subjcombid,
            'subjlist':subjlist,
            'mpadd':True,
            'mplist':classsubject.objects.filter(clscd=clas.id)

            }
            return render(request,'classsubject.html',context)
        elif 'save' in request.POST:
            mpid = int(request.POST['mpid'])
            sub=int(request.POST['sub'])
            clscd = int(request.POST['clcd'])
            clasrec=classmas.objects.get(id=clscd)
            subrec=subjmas.objects.get(id=sub)
            tmark = int(request.POST['tmark'])
            amark= int(request.POST['amark'])
            pmark= int(request.POST['pmark'])
            combid=int(request.POST['comb'])
            
            if mpid == 0:
                mprec = classsubject(clscd=clasrec,subj=subrec,tmm=tmark,pmm=pmark,amm=amark,subjcombid=combid)
            else:
                mprec= classsubject.objects.get(id = mpid)
                mprec.tmm = tmark
                mprec.amm=amark
                mprec.pmm=pmark
                mprec.subjcombid=combid

            mprec.save()
            context = {
                'cllist':cllist,
                'subjlist':subjlist,
                'maplist':classsubject.objects.filter(clscd=clasrec.id),
                'clselect':False,
                'mpadd':False,
                'clcd':clasrec.id

            }
            return render(request,'classsubject.html',context)

    context ={
        'cllist':cllist,
        'subjlist':subjlist,
        'maplist':maplist,
        'clselect':False,
        'clcd':clcd
    }

    return render(request,'classsubject.html',context)

def studentreg(request):
    stsexchoices = (('M','Male'),('F','Feamle'),('O','Other/लागू नहीं'))
    streligionchoices = (('H','Hindu'),('M','Muslim'),('S','Sikh'),('C','Christian'))
    stcatchoices = (('G','General'),('O','OBC'),('S','SC'),('T','ST'),('H','General IRDP'),('I','OBC IRDP'),('J','SC IRDP'),('K','ST IRDP'),('N','Not Applicable'))
    statuschoices=(('A','Admitted'),('E','Pending'),('L','SLC'))
    bldchoices=(('A','A+'),('A1','A-'),('B','B+'),('B1','B-'),('O','O+'),('O1','O-'),('AB','AB+'),('AB1','AB-'),('Z','Not Known'))
    cllist= classmas.objects.all()
    statelist=statemas.objects.all()
    if request.method=='POST':
        print(request.POST)
        stcd=int(request.POST['stnm'])
        clcd=int(request.POST['cls'])
        sexcd=(request.POST['gend'])
        relgcd=(request.POST['rlg'])
        scast=request.POST['scat']
        bldcd=request.POST['sbld']

        if request.POST['dis'] == 'Choose...':
            strec=statemas.objects.get(id=stcd)
            dislist=disttmas.objects.filter(scode=strec.id)
            context={
                'sex':stsexchoices,
                'rlglist':streligionchoices,
                'cstlist':stcatchoices,
                'bldlist':bldchoices,
                'clslist':cllist,
                'stlist':statelist,
                'dislist':dislist,
                'clcd':clcd,
                'sexcd':sexcd,
                'sex':stsexchoices,
                'bldlist':bldchoices,
                'rlgcd':relgcd,
                'rlglist':streligionchoices,
                'cstlist':stcatchoices,
                'scast':scast,
                'bldcd':bldcd,
                'stcd':strec.id
                }                
            return render(request,"studentreg.html",context)
        elif request.POST['teh'] == 'Choose...':
            stcd=int(request.POST['stnm'])
            strec=statemas.objects.get(id=stcd)
            discd=int(request.POST['dis'])
            disrec=disttmas.objects.get(id=discd)
            dislist=disttmas.objects.filter(scode=strec.id)
            tehlist=tehmas.objects.filter(disttcd=disrec.id)
            context= {
                    
                'stcd':strec.id,
                'discd':discd,
                'dislist':dislist,
                'stlist':statelist,
                'tehlist':tehlist,
                'clslist':cllist,
                'sexcd':sexcd,
                'sex':stsexchoices,
                'rlglist':streligionchoices,
                'rlgcd':relgcd,
                'scast':scast,
                'cstlist':stcatchoices,
                'bldlist':bldchoices,
                'bldcd':bldcd,
                'clcd':clcd
            }
            return render(request,"studentreg.html",context)
        elif request.POST['pan'] == 'Choose...':
            stcd=int(request.POST['stnm'])
            strec=statemas.objects.get(id=stcd)
            discd=int(request.POST['dis'])
            tehcd=int(request.POST['teh'])
            tehrec=tehmas.objects.get(id=tehcd)
            disrec=disttmas.objects.get(id=discd)
            dislist=disttmas.objects.filter(scode=strec.id)
            tehlist=tehmas.objects.filter(disttcd=disrec.id)
            panlist=panchayatmas.objects.filter(tehcd=tehrec.id)
            context= {
                    
                'stcd':strec.id,
                'discd':discd,
                'dislist':dislist,
                'stlist':statelist,
                'tehlist':tehlist,
                'clslist':cllist,
                'clcd':clcd,
                'tehcd':tehrec.id,
                'sexcd':sexcd,
                'sex':stsexchoices,
                'rlglist':streligionchoices,
                'rlgcd':relgcd,
                'scast':scast,
                'cstlist':stcatchoices,
                'bldcd':bldcd,
                'bldlist':bldchoices,
                'panlist':panlist
            }
            return render(request,"studentreg.html",context)

        else:
            pass

    context={
         'sex':stsexchoices,
         'rlglist':streligionchoices,
         'cstlist':stcatchoices,
         'bldlist':bldchoices,
         'clslist':cllist,
         'stlist':statelist,
         
         
     }
    return render(request,"studentreg.html",context)

