
from django.contrib import admin
from django.urls import path,include
from prof_section import views 
from django.conf.urls import url,include

urlpatterns = [
    
    url(r'^admin/', admin.site.urls),
    url(r'prof_section/',include('prof_section.urls')),
    url(r'stu_section/',include('stu_section.urls')),
    url(r'^$',views.welcome, name= "welcome" ),
    url(r'^records/', views.records, name="records"),
]
