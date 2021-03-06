
from django.contrib import admin
from django.urls import path,include
from prof_section import views 
from django.conf.urls import url,include
from django.conf import settings

urlpatterns = [
    
    url(r'^admin/', admin.site.urls),
    url(r'prof_section/',include('prof_section.urls')),
    url(r'stu_section/',include('stu_section.urls')),
    url(r'^$',views.welcome, name= "welcome" ),
    url(r'^records/', views.records, name="records"),
]


if settings.DEBUG:
	import debug_toolbar

	urlpatterns = urlpatterns + [

		url(r'^__debug__/', include(debug_toolbar.urls))

	 ]