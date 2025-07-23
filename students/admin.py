from django.contrib import admin
from .models import Student

class StudentAdmin(admin.ModelAdmin):
    search_fields = ('name', 'email')  # Enables search by name or email in admin

# Register with custom admin
admin.site.register(Student, StudentAdmin)
