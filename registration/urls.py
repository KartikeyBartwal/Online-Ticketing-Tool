"""registration URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app1 import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.SignupPage,name = "signup"),

    path('login/',views.LoginPage,name='login'),

    path('home/',views.HomePage,name="home"),
         
    path('home/File ticket',views.FileticketPage,name = "FileTicket"),
         
    path('home/FAQ',views.FAQPage,name = "FAQ"),
    
    path("home/File ticket/Ticket History",views.TicketHistoryPage,name = "Ticket History"),
    
    path("home/premium",views.premium,name = "Premium"),
    path("home/Company",views.Company,name = "Company"),
         
    path("home/free",views.free,name = "free"),
    
    path("home/PremiumTicket",views.premiumticket,name = "Premium Ticket"),
         
    path("home/CompanyTicket",views.companyticket,name = "Company Ticket"),
         
    # For admins
    path('admin/AdminDashboard',views.AdminDashboard,name = "Admin Dashboard"),
         
    path('f',views.AdminTicketDashboard,name = "Admin Ticket Dashboard"),
]
