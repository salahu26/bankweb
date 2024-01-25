from . import views
from  django.urls import path
from .views import login, forms, branch, message, Kasaragod, Kannur,Idukki, Ernakulam, Alappuzha
app_name = 'regapp'



urlpatterns = [
    path('register',views.register,name='register'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),
    path('branch/', branch, name='branch'),
    path('form/', forms, name='form'),
    path('Alappuzha/', views.Alappuzha, name='Alappuzha'),
    path('Ernakulam/', Ernakulam, name='ER'),
    path('Idukki/', Idukki, name='ID'),
    path('Kannur/', Kannur, name='KN'),
    path('Kasaragod/', Kasaragod, name='KS'),
    path('message/', message, name='message'),
    path('forms/', forms, name='forms'),

]