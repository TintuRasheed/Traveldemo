from .import views
from django.urls import path

urlpatterns = [
    path('',views.demo,name='demo'),
   
     # path('About/',views.About,name="About"),
     # path('Contact/',views.Contact,name="Contact"),
    path('',views.NumAdd,name='NumAdd'),
    path('add/',views.Addition,name='Addition')
 ]  
