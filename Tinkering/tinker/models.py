from django.db import models
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.db.models.signals import post_save


Departments = (
('Architecture and Planning','Architecture and Planning'),
('Applied Science and Engineering','Applied Science and Engineering'),
('Biotechnology','Biotechnology'),
('Chemical Engineering','Chemical Engineering'),
('Chemistry','Chemistry'),
('Civil Engineering','Civil Engineering'),
('Computer Science and Engineering','Computer Science and Engineering'),
('Earthquake Engineering','Earthquake Engineering'),
('Earth Sciences','Earth Sciences'),
("Electrical Engineering",'Electrical Engineering'),
('Electronics and Communication Engineering','Electronics and Communication Engineering'),
('Humanities and Social Sciences','Humanities and Social Sciences'),
('Hydrology','Hydrology'),
('Management Studies','Management Studies'),
('Mathematics','Mathematics'),
('Mechanical and Industrial Engineering','Mechanical and Industrial Engineering'),
('Metallurgical and Materials Engineering','Metallurgical and Materials Engineering'),
('Paper Technology','Paper Technology'),
('Polymer and Process Engineering','Polymer and Process Engineering'),
('Physics','Physics'),
('Water Resources Development and Managemen','Water Resources Development and Management')

)


Programs = (
            ("B.Tech","B.Tech"),
            ("M.Tech","M.Tech"),
            ("IDD","IDD"),
            ("Ph.D","Ph.D"),
            ("MSc.","MSc." ),
            ("BSc.","BSc."),
            ("MBA","MBA"),
            ("B.Arch.","B.Arch."),
)



facility = (

    ('3d_print', "3D Printer") ,
    ('projet' ,"3D System's Projet MJP 3600" ) ,
    ( 'bozxy' , "Laser Etcher BOXZY"),
    ('carvy'," Carving Machines Carvey"),
    ('powe',"Power Tools (Saw, Jigsaw, Drill)"),
    ("elec",'Electronics Facility'),
    ("pc","Workstations"),
    ('cnc',"CNC Lathe"),
    ('clave',"Autoclave"),
    ("VMC","VMC")
)

yes_no = (

    ("YES" , "YES"),
    ("NO","No")
)

cat = (

    ("3dp","3D Printers "),
    ("3ds","3D Scanner"),
    ("adm","Advanced Machines "),
    ("elec",'Electronics Facilities'),
    ("Comp","Computer Facilities"),
    ("power","Power Tools"),
    ("soft","Softwares"),
    ("fla","Filament"),
    ("cl","Clamp"),
    ("sheets","Sheets"),
    ("tools","Tools"),
    ("Sandpaper","Sandpaper"),
    ("chem","Chemicals"),
    ("Safety","Safety Equipments"),
    ("Misc","Miscellaneuos")

)

worksation_t  = (
    ('Xeon','Xeon'),
    ("I7","I7")
)

source = (
    ("Personal Project","Personal Project"),
    ("Clubs","Clubs"),
    ("Professor","Professor")
)
class User_Data (models.Model):

    user = models.OneToOneField(User,  on_delete=models.CASCADE)
    Er_No = models.BigIntegerField(default="0")
    Dep = models.CharField(choices=Departments , default = "Select Your Department", max_length = 1000)
    Mob_No = models.BigIntegerField(default="0")
    program = models.CharField(default="Enter your Department" , choices=Programs, max_length = 1000)
 
def create_profile (sender , **kwargs):
    if kwargs['created']:
        user_profile = User_Data.objects.create(user = kwargs['instance'])
post_save.connect(create_profile,sender = User) 
class inventory (models.Model):
    Name = models.CharField(default="Product Name ", max_length=200)
    Quantity = models.IntegerField()
    working = models.IntegerField()
    allocated = models.IntegerField()
    category =  models.CharField(default="", max_length=200, choices=cat )
    unit = models.CharField(default="", max_length=100)
class worksation(models.Model):
    # Auto add from user model
    #user = models.ForeignKey(User,on_delete=models.CASCADE )
    Eroll_No = models.BigIntegerField(default="0", name="Enrollment Number")
    name = models.CharField(max_length=1000, name= "Name")
    Mob_No = models.BigIntegerField(default="0" , name = "Mobile Number")
    email = models.EmailField(max_length=1000 , default='')
    #Will be added by Staff
    allocated = models.CharField(choices=yes_no,  max_length = 20)
    start_date = models.DateField(null=True )
    end_date = models.DateField(null=True )
    Workstation_No = models.CharField(max_length=100, name = "Workstation Number")
    Workstation_type = models.CharField(max_length=1000, choices=worksation_t, name="Select Workstation Type")
    # Ask from Users
    Project_Supervisor = models.CharField(max_length=100, choices=source, default="")
    Use_of_Workstation = models.CharField(max_length=1000)
    Number_of_days_you_want_to_work = models.IntegerField(default=1)

class project(models.Model):

    Eroll_No = models.BigIntegerField(default="0", name="Enrollment Number")
    name = models.CharField(max_length=100, name= "Name")
    Mob_No = models.BigIntegerField(default="0" , name = "Mobile Number")
    email = models.EmailField(max_length=1000 , default='')


    Project_Name = models.CharField(  max_length=200, default = "")
    Project_Description = models.TextField( max_length=1000, default = "")
    Facilities_Required= models.CharField (  max_length = 200 , choices = facility, default = "")
    Project_Supervisor  = models.CharField( max_length = 100 , choices = source, default = "")
    #porject_permission =


class feedback(models.Model):
    Eroll_No = models.BigIntegerField(default="0", name="Enrollment Number")
    name = models.CharField(max_length=100, name="Name")
    Mob_No = models.BigIntegerField(default="0", name="Mobile Number")
    email = models.EmailField(max_length=1000, default='')


    #user enters
    What_did_you_do_in_Tinkering_Lab = models.TextField(max_length=1000, default="")
    Any_Complaints = models.TextField(max_length=1000, default="")
    Suggestions_for_New_Equipment_or_Software_Required = models.CharField(max_length=200, default="")
    Suggestions_for_improvement = models.TextField(max_length=1000, default="")




class project_for_display(models.Model):
    name = models.CharField(max_length=1000, name="Name", default='')
    title=models.CharField(max_length=1000, default='')
    status = models.CharField(max_length=100, default='')
