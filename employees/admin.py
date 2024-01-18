from django.contrib import admin
from .models import Employee, Department, Post, Staff, Message
# Register your models here.

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'department']


class PostAdmin(admin.ModelAdmin):
    list_display = ['author', 'title', 'posttype', 'created_at']

class MessageAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject']

# class EmployeeAdmin(admin.ModelAdmin):
#     list_display = ['first_name', 'last_name', 'department']


admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Department)
admin.site.register(Post, PostAdmin)
admin.site.register(Staff)
admin.site.register(Message, MessageAdmin)