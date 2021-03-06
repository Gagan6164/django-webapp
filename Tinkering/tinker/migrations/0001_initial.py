# Generated by Django 2.0.6 on 2018-07-17 08:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Enrollment Number', models.BigIntegerField(default='0')),
                ('Name', models.CharField(max_length=100)),
                ('Mobile Number', models.BigIntegerField(default='0')),
                ('email', models.EmailField(default='', max_length=1000)),
                ('What_did_you_do_in_Tinkering_Lab', models.TextField(default='', max_length=1000)),
                ('Any_Complaints', models.TextField(default='', max_length=1000)),
                ('Suggestions_for_New_Equipment_or_Software_Required', models.CharField(default='', max_length=200)),
                ('Suggestions_for_improvement', models.TextField(default='', max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='inventory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(default='Product Name ', max_length=200)),
                ('Quantity', models.IntegerField()),
                ('working', models.IntegerField()),
                ('allocated', models.IntegerField()),
                ('category', models.CharField(choices=[('3dp', '3D Printers '), ('3ds', '3D Scanner'), ('adm', 'Advanced Machines '), ('elec', 'Electronics Facilities'), ('Comp', 'Computer Facilities'), ('power', 'Power Tools'), ('soft', 'Softwares'), ('fla', 'Filament'), ('cl', 'Clamp'), ('sheets', 'Sheets'), ('tools', 'Tools'), ('Sandpaper', 'Sandpaper'), ('chem', 'Chemicals'), ('Safety', 'Safety Equipments'), ('Misc', 'Miscellaneuos')], default='', max_length=200)),
                ('unit', models.CharField(default='', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Enrollment Number', models.BigIntegerField(default='0')),
                ('Name', models.CharField(max_length=100)),
                ('Mobile Number', models.BigIntegerField(default='0')),
                ('email', models.EmailField(default='', max_length=1000)),
                ('Project_Name', models.CharField(default='', max_length=200)),
                ('Project_Description', models.TextField(default='', max_length=1000)),
                ('Facilities_Required', models.CharField(choices=[('3d_print', '3D Printer'), ('projet', "3D System's Projet MJP 3600"), ('bozxy', 'Laser Etcher BOXZY'), ('carvy', ' Carving Machines Carvey'), ('powe', 'Power Tools (Saw, Jigsaw, Drill)'), ('elec', 'Electronics Facility'), ('pc', 'Workstations'), ('cnc', 'CNC Lathe'), ('clave', 'Autoclave'), ('VMC', 'VMC')], default='', max_length=200)),
                ('Project_Supervisor', models.CharField(choices=[('Personal Project', 'Personal Project'), ('Clubs', 'Clubs'), ('Professor', 'Professor')], default='', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='project_for_display',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(default='', max_length=1000)),
                ('title', models.CharField(default='', max_length=1000)),
                ('status', models.CharField(default='', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='User_Data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Er_No', models.BigIntegerField(default='0')),
                ('Dep', models.CharField(choices=[('Architecture and Planning', 'Architecture and Planning'), ('Applied Science and Engineering', 'Applied Science and Engineering'), ('Biotechnology', 'Biotechnology'), ('Chemical Engineering', 'Chemical Engineering'), ('Chemistry', 'Chemistry'), ('Civil Engineering', 'Civil Engineering'), ('Computer Science and Engineering', 'Computer Science and Engineering'), ('Earthquake Engineering', 'Earthquake Engineering'), ('Earth Sciences', 'Earth Sciences'), ('Electrical Engineering', 'Electrical Engineering'), ('Electronics and Communication Engineering', 'Electronics and Communication Engineering'), ('Humanities and Social Sciences', 'Humanities and Social Sciences'), ('Hydrology', 'Hydrology'), ('Management Studies', 'Management Studies'), ('Mathematics', 'Mathematics'), ('Mechanical and Industrial Engineering', 'Mechanical and Industrial Engineering'), ('Metallurgical and Materials Engineering', 'Metallurgical and Materials Engineering'), ('Paper Technology', 'Paper Technology'), ('Polymer and Process Engineering', 'Polymer and Process Engineering'), ('Physics', 'Physics'), ('Water Resources Development and Managemen', 'Water Resources Development and Management')], default='Select Your Department', max_length=1000)),
                ('Mob_No', models.BigIntegerField(default='0')),
                ('program', models.CharField(choices=[('B.Tech', 'B.Tech'), ('M.Tech', 'M.Tech'), ('IDD', 'IDD'), ('Ph.D', 'Ph.D'), ('MSc.', 'MSc.'), ('BSc.', 'BSc.'), ('MBA', 'MBA'), ('B.Arch.', 'B.Arch.')], default='Enter your Department', max_length=1000)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='worksation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Enrollment Number', models.BigIntegerField(default='0')),
                ('Name', models.CharField(max_length=1000)),
                ('Mobile Number', models.BigIntegerField(default='0')),
                ('email', models.EmailField(default='', max_length=1000)),
                ('allocated', models.CharField(choices=[('YES', 'YES'), ('NO', 'No')], max_length=20)),
                ('start_date', models.DateField(null=True)),
                ('end_date', models.DateField(null=True)),
                ('Workstation Number', models.CharField(max_length=100)),
                ('Select Workstation Type', models.CharField(choices=[('Xeon', 'Xeon'), ('I7', 'I7')], max_length=1000)),
                ('Project_Supervisor', models.CharField(choices=[('Personal Project', 'Personal Project'), ('Clubs', 'Clubs'), ('Professor', 'Professor')], default='', max_length=100)),
                ('Use_of_Workstation', models.CharField(max_length=1000)),
                ('Number_of_days_you_want_to_work', models.IntegerField(default=1)),
            ],
        ),
    ]
