from django.urls import path
from .import views
app_name = 'students'
urlpatterns = [
   
    path('',views.index,name="index"),
    path('process_contactus/',views.process_contactus,name="process_contactus"),
   # path('aboutus/',views.aboutus,name='aboutus'),
  #  path('home/',views.home,name='home'),
]