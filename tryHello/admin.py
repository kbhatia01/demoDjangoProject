from django.contrib import admin

from tryHello.models import Student, Enrollment, Course

# Register your models here.


admin.site.register(Enrollment)
admin.site.register(Course)


class StudentAdmin(admin.ModelAdmin):
    list_filter = (('name'),)
    list_display = ('name', 'age')
    list_editable = (('age'),)
    ordering = (('age'),)

admin.site.register(Student, StudentAdmin)
