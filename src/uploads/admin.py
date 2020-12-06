from django.contrib import admin

from .models import upload

class upload_admin(admin.ModelAdmin):
	
	list_display = ('title','subject','curriculum', 'date')
	list_filter = ('date',)

# admin.site.register(upload,upload_admin)
