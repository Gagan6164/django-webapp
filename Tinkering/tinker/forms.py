from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import  worksation, project, feedback



Departments = (
('Archi','Architecture and Planning'),
('appliedsci','Applied Science and Engineering'),
('bio','Biotechnology'),
('chemical','Chemical Engineering'),
('chem','Chemistry'),
('civil','Civil Engineering'),
('cse','Computer Science and Engineering'),
('earthquake','Earthquake Engineering'),
('earth','Earth Sciences'),
("elec",'Electrical Engineering'),
('ece','Electronics and Communication Engineering'),
('human','Humanities and Social Sciences'),
('hydro','Hydrology'),
('managemnt','Management Studies'),
('math','Mathematics'),
('mech','Mechanical and Industrial Engineering'),
('meta','Metallurgical and Materials Engineering'),
('paper','Paper Technology'),
('poly','Polymer and Process Engineering'),
('phy','Physics'),
('water','Water Resources Development and Management')

)

Programs = (
            ("B.Tech","B.Tech"),
            ("M.Tech","M.Tech"),
            ("IDD","IDD"),
            ("Ph.D","Ph.D"),
            ("MSc.","MSc." ),
            ("BSc.","BSc."),
            ("MBA","MBA")
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

    ("y" , "YES"),
    ("n","No")
)

worksation_t  = (
    ('Xeon','Xeon'),
    ("I7","I7")
)

source = (
    ("Personal Use","Personal Use"),
    ("Group Project","Group Project"),
    ("Project Under Proff","Project Under Proff")
)

class NameForm(UserCreationForm):
    Er_No = forms.IntegerField(required = True, label="Enter Your Enrollment Number")
    email = forms.EmailField(required=True , label="Enter your Email address")

    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2',
            'Er_No'
        )

    def save(self, commit=True):
        users = super(NameForm, self).save(commit=False)
        users.first_name = self.cleaned_data['first_name']
        users.last_name = self.cleaned_data['last_name']
        users.email = self.cleaned_data['email']
        if commit:
            users.save()
        return users
 


     

class contact(forms.Form):
    name = forms.CharField(label="Name:")
    email = forms.EmailField(label ="Email") 
    subject = forms.CharField(label = "Subject:")
    message = forms.CharField(label = "What would you like to share?",widget=forms.Textarea)



class workstation_form(forms.ModelForm):

    use = forms.ChoiceField(choices=source , label = "Project Supervisor: ")
    no_of_days = forms.IntegerField (  label = "Number of days required:",)
    des = forms.CharField( label = "Describe Why you need this workstation? " ,widget=forms.Textarea)
    class Meta:
        model = worksation
        fields =(
            'use',
            'no_of_days',
            'des',

                )






class pro(forms.ModelForm):
    class Meta :
        model = project
        fields = (
            'Project_Name',
            'Project_Description',
            'Facilities_Required',
            'Project_Supervisor',
        )




class feed(forms.ModelForm):
    class Meta:
        model = feedback
        fields = (

            'What_did_you_do_in_Tinkering_Lab',
            'Any_Complaints',
            'Suggestions_for_New_Equipment_or_Software_Required',
            'Suggestions_for_improvement',
        )