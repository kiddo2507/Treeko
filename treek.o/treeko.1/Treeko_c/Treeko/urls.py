from django.urls import path
from . import views
urlpatterns = [path('',views.home,name='home'),
   path('customer_signin_left.html',views.login,name='login'),
   path('register',views.register,name="register"),
   path('login',views.login, name='login'),
   path('homepage_admin.html',views.homepage_admin, name='homepage_admin'),
   path('homepage_customer.html',views.homepage_customer,name="homepage_customer.html"),
   path('home_c',views.homepage_customer,name='homepage_customer'),
   path('home_a',views.homepage_admin,name='homepage_admin'),
   path('home',views.home,name='home'),
   path('about.html',views.about,name='about'),
   path('2ndpage_customer.html',views.two_customer,name='2ndpage_customer.html'),
   path('newrequest-customer.html',views.newrequest_sub,name='newrequest-customer.html'),
   path('add_proof',views.add_proof,name='add_proof'),
   path('check_request',views.check_request,name='check_request'),
   path('check_proof',views.check_proof,name='check_proof'),
   path('checkrequest2',views.checkrequest2,name='checkrequest2'),
   path('generate_page',views.generate_page,name="generate_page"),
   path('newrequest',views.newrequest_sub,name="newrequest_sub"),
   path('submit_proof',views.add_proof,name="adding proof")

   ]
