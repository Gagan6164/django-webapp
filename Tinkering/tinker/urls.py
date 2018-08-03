from django.urls import path,include
from django.conf.urls import url
from django.contrib.auth.views import login,logout
from django.conf.urls.static import static
from Tinkering import settings
from django.views.generic.base import RedirectView


from .import views

urlpatterns = [

    path('', views.index),
    path('Home', views.index),
    path('Notes', views.notes),
    path('Facilities', views.facility),
    path('Projects', views.Project_List),
    path('faq', views.faq),
    path('About', views.About_US),
    path('updates', views.update),
    path('team', views.team),
    path("register", views.register),
    url(r'^login$',login,{'template_name':'login.html'}),
    url(r'^logout$',logout,{'template_name':'logout.html'}),
    path('contact', views.talk),
    path('accounts/profile/',views.profile),
    path('accounts/profile/project', views.proje),
    path('accounts/profile/My_Profile', views.myprof),
    path('accounts/profile/feedback', views.feedback_form),
    url(r"^accounts/profile/Workstation-Booking$",views.Workstation , name="work"),
    path('3DPrinter', views.D_Printer),
    path('3DScanner', views.D_Scanner),
    path('Laser', views.laser),
    path('Metal-Milling', views.metal_milling),
    path('Electronics', views.Electronics),
    path('Wood-Milling', views.wood_milling),
    url(r'^', include('favicon.urls'))
    
    


]+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
