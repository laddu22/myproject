from django.contrib import admin
from todolist_app.models import Tasklist,request_from_contact,request_call
from .models import CustomUser
# Register your models here.




class TasklistAdmin(admin.ModelAdmin):
    class meta:
        model=Tasklist
        list_display = ('Task')




admin.site.register(CustomUser)
admin.site.register(Tasklist,TasklistAdmin)
admin.site.register(request_from_contact)
admin.site.register(request_call)