from django.contrib import admin
from .models import User_Data,inventory,project,worksation,project_for_display


class BookAdmin(admin.ModelAdmin):
    list_display= ('Name', 'Quantity', 'working', 'allocated','category','unit')
admin.site.register(inventory,BookAdmin)


class UserData2(admin.ModelAdmin):
    
    list_display= ('user',  'Er_No', 'Dep', 'Mob_No','program')

 
admin.site.register(User_Data,UserData2)





admin.site.register(project)
admin.site.register(worksation)
admin.site.register(project_for_display)