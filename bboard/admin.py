from django.contrib import admin
from .models import Bb
from .models import Rubric


class BbAdmin(admin.ModelAdmin):
    list_display = ('title', 'rubric', 'description', 'price', 'date')
    list_display_links = ('title', 'description')
    search_fields = ('title', 'description')


admin.site.register(Bb, BbAdmin)
admin.site.register(Rubric)
