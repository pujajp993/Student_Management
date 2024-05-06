from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('',views.home,name='home'),
    path('adminhome',views.adminhome,name='adminhome'),

    #student
    path('studenthome',views.studenthome,name='studenthome'),

    path('regstudent',views.regstudent,name='regstudent'),
    path('studlist',views.studlist,name='studlist'),
    path('studapprove/<int:id>/',views.studapprove),
    path('studreject/<int:id>/',views.studreject),
    
    
    path('teacherhome',views.teacherhome,name='teacherhome'),
    path('regteacher',views.regteacher,name='regteacher'),
    path('teacherlist',views.teacherlist,name='teacherlist'),
    path('log',views.log,name='log'),
]
