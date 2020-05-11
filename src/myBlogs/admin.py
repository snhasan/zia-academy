from django.contrib import admin

from .models import myBlog


admin.site.site_header = 'Ziaul Commercial Learning'

class myBlog_admin(admin.ModelAdmin):
	
	list_display = ('title', 'date')
	list_filter = ('date',)

admin.site.register(myBlog,myBlog_admin)