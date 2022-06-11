from django.contrib import admin

from tasks.models import Category,Status,Task

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)

class StatusAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)

class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'title',)

admin.site.register(Category, CategoryAdmin)
admin.site.register(Task, TaskAdmin)
admin.site.register(Status, CategoryAdmin)
