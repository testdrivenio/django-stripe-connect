from django.contrib import admin

from .models import Course


class CourseAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'title', 'price', 'fee', 'seller', 'created_at',
        'updated_at',
    )
    readonly_fields = ('id',)


admin.site.register(Course, CourseAdmin)
