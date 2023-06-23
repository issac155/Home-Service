from django.urls import path
from . import views
#from .views import delete_location
#from .views import delete_worker



urlpatterns = [
    path('', views.register, name='register'),
    path('otp', views.otpVerify, name='otp'),
    path('index', views.index, name='index'),
    path('login',views.login,name='login'),
    path('ser', views.search1, name='ser'),
    path('res',views.result,name='res'),
    path('fe',views.login,name='fe'),
    path('hi',views.logout_view,name='hi'),
    path('bi/<int:result_id>/',views.request,name='bi'), 
    path('had',views.cust,name='had'),
    path('iss',views.li,name='iss'),
    path('hai',views.hai,name='hai'),
    path('Booking',views.approved_customers,name='Booking'),
    
]