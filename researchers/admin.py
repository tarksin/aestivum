from django.contrib import admin
from .models import Researcher

class ResearcherAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name','academic_title', 'featured')
    list_display_links = ('first_name', 'last_name','academic_title')
    

admin.site.register(Researcher, ResearcherAdmin)