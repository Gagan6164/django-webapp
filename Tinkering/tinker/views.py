from django.shortcuts import render
from django.http import HttpResponseRedirect
from  .forms import NameForm,contact,workstation_form,pro,feedback
from .models import project_for_display

def D_Printer(request):
    return render(request, '3dprinter.html', {'title':"3D Printers ", 'user' : request.user,'page':"3D Printer" } )
def D_Scanner(request):
    return render(request, '3dscanner.html', {'title':"3D Scanner ", 'user' : request.user,'page':"3D Scanner" } )
def laser(request):
    return render(request, 'laserd.html', {'title':"Laser Ecthing ", 'user' : request.user,'page':"Laser Ecthing" } )
def metal_milling(request):
    return render(request, 'metald.html', {'title':"Metal Milling ", 'user' : request.user,'page':"Metal Milling" } )
def Electronics(request):
    return render(request, 'electro.html', {'title':"Electronics ", 'user' : request.user,'page':"Electronics" } )
def wood_milling(request):
    return render(request, 'wood.html', {'title':"Wood Milling ", 'user' : request.user,'page':"Wood Milling" } )












def index(request):
    return render(request,"index.html", {'title' : "The Tinkering Lab ", 'user' : request.user,'page':"Home"})
def profile(request):
    return render(request, 'profile.html', {'title':"My Account" , 'user' : request.user,'page':"My Account"} )
def About_US(request):
    return render(request, 'vision.html', {'title':"About Us", 'user' : request.user,'page':"About Us" } )
def team(request):
    return render(request, 'team.html', {'title':"Our Team ", 'user' : request.user,'page':"Our Team " } )
def faq(request):
    return render(request, 'faq.html', {'title':"FAQ ", 'user' : request.user,'page':"FAQs" } )
def update(request):
    return render(request, 'updates.html', {'title':"Updates ", 'user' : request.user, 'page':"Updates"} )
def notes(request):
    return render(request, 'notes.html', {'title':"Notes ", 'user' : request.user, 'page':"Notes"} )
def facility(request):
    return render(request, 'facility.html', {'title':"Facilities ", 'user' : request.user, 'page':"Facilities"} )
def Project_List(request):
    data = project_for_display.objects.all()
    return render(request, 'proj.html', {'title':"Project List  ", 'user' : request.user, 'page':"Projects",'data':data} )

def myprof(request):

    return render(request, 'profile_details.html', {'title':"My Profile ", 'user' : request.user,} )





def talk(request):
    if request.method == 'POST':
        form = contact(request.POST)
        if form.is_valid():
            name = request.user.first_name
            email = request.user.email
            subjects = request.POST.get('subject','')
            desc = request.POST.get('message','')
            ''' 
            email = EmailMessage(
                subject = subjects,
                message = 'This Email is from Contact form of the Tinkering Lab Website\n' + message,
                from_email= email,
                to = 'rethink.Tinkering@gmail.com',
                fail_silently = False

            )
            '''
             



    else:
        form = contact()
    return render(request, "talk.html", {'title': " Talk To Us " , 'form':form, 'user' : request.user,'page':"Contact Us"})



def register(request):
    if request.method == 'POST':
        form3 = NameForm(request.POST)
        form3.save()
    else:
        form3 = NameForm()
    return render(request, 'register.html', {'form3': form3 ,'title':"Register here", 'user' : request.user,'page':"Registration"})

def Workstation(request):
    if request.method == 'POST':
        form =  workstation_form(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'thanks.html')
        else :
            print(form.errors)
    else:
        form = workstation_form()
    return render(request, 'worstation.html', {'title':"Workstation Booking" , 'user' : request.user,'form': form,'page':"Workstation Booking",
                                               'text' :'Just a small step then you are ready to go'} )
def proje(request):
    if request.method == 'POST':
        form = pro(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'thanks.html')
        else:
            return render(request, 'thanks3.html')
    else:
        form = pro()
    return render(request, 'project.html', {'title': "Start a Project", 'user': request.user, 'form': form,'page':"Project"})

def feedback_form(request):

    if request.method == 'POST':
        form =  feedback(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'thanks.html')
        else :
            print(form.errors)
    else:
        form = feedback()
    return render(request, 'worstation.html', {'title':"Feedback " , 'user' : request.user,'form': form,'page':"Feedback Form",
                                               'text' :'Please fill the following details '} )



























def access(request):
    if request.method == 'POST':
        form = NameForm(request.POST)
        return HttpResponseRedirect('/thanks/')
    else:
        form = NameForm()
    return render(request, 'access.html', {'form': form},{'title' : "The Tinkering Lab "})

