
from django.urls import path
from.import views
urlpatterns = [
path('registeration',views.userregisteration,name='registeration'),
path('',views.login,name='login'),
path('index',views.index,name='index'),
path('user',views.user,name='user'),
path('userdetaillist/<int:user_id>',views.userdetaillist,name='userdetaillist'),
path('Academicdetails',views.Academicdetails,name='Academicdetails'),
path('eduacationaldetails',views.createedu,name='eduacationaldetails'),
path('vieweduacationaldetails',views.detailedu,name='vieweducationaldetails'),
path('updateeduacationaldetails/<int:eid>',views.updateeducationaldetails,name='updateeducationaldetails'),
path('deleteeduacationaldetails/<int:eid>',views.deleteedu,name='deleteeducationaldetails'),
path('skills', views.skills, name='skills'),
path('exp', views.experience, name='exp'),
path('projectdetails',views.projectdetails,name='projectdetails'),
path('certification',views.certification,name='certification'),
path('createcertification',views.createcert,name='createcertification'),
path('viewcertificationdetails',views.detailcert,name='viewcertificationdetails'),
path('updatecertificationdetails/<int:eid>',views.updatecert,name='updatecertificationdetails'),
path('deletecertificationdetails/<int:eid>',views.deletecert,name='deletecertificationdetails'),
path('createskill',views.createskill,name='createskill'),
path('viewskilldetails',views.detailskill,name='viewskilldetails'),
path('updateskilldetails/<int:eid>',views.updateskill,name='updateskilldetails'),
path('deleteskilldetails/<int:eid>',views.deleteskill,name='deleteskilldetails'),
path('createexp',views.createexp,name='createexperience'),
path('viewexpdetails',views.detailexp,name='viewexperiencedetails'),
path('updateexpdetails/<int:eid>',views.updateexp,name='updateexpdetails'),
path('logout',views.logout,name='logout'),
path('deleteexpdetails/<int:eid>',views.deleteexp,name='deleteexpdetails')

# path('profile/<int:id>/', views.profile, name='profile')
]
