from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

from home import views

urlpatterns = [
  path("",views.index,name='home'),
  path("about",views.about,name='about'),
  path("contact",views.contact,name='contact'),
  path("service",views.service,name='service'),
  path("add",views.add, name="add"),
  path("staffadd/<catr>",views.staffadd,name='staffadd'),
  path("staff/<cat>",views.Staff,name='Staff'),
  path("masterentry",views.mentry,name='mentry'),
  path("updatetehsil",views.addedittehsil,name='updatetehsil'),
  path("updatepanch", views.addeditpanchyat,name='updatepanch'),
  path("updatedistt", views.addeditdistt,name='updatedistt'),
  path("updatesubject",views.addeditsubject,name="updatesubject")

  
]
urlpatterns =urlpatterns+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT )

