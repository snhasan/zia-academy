from django.contrib import admin

from .models import About,Team,faq,services,Profile,Gallery,Activitie,Program,ContactForm,Home_Image

class About_admin(admin.ModelAdmin):
	
	list_display = ('title', 'date')
	list_filter = ('date',)

class Team_admin(admin.ModelAdmin):
	
	list_display = ('name', 'designation')
	list_filter = ('date',)


class faq_admin(admin.ModelAdmin):
	
	list_display = ('question', )
	list_filter = ('date',)


class service_admin(admin.ModelAdmin):
	
	list_display = ('title', )
	list_filter = ('date',)


class Profile_admin(admin.ModelAdmin):
	
	list_display = ('name', )
	list_filter = ('date',)


class Gallery_admin(admin.ModelAdmin):
	
	list_display = ('title', )
	list_filter = ('date',)


class Activitie_admin(admin.ModelAdmin):
	
	list_display = ('title', 'date')
	list_filter = ('date',)


class Program_admin(admin.ModelAdmin):
	
	list_display = ('title', 'date')
	list_filter = ('date',)


class ContactForm_admin(admin.ModelAdmin):
	
	list_display = ('name', 'date')
	list_filter = ('date',)


class Home_Image_admin(admin.ModelAdmin):
	
	list_display = ('title', 'date')
	list_filter = ('date',)


admin.site.register(About,About_admin)
admin.site.register(Profile,Profile_admin)
admin.site.register(Gallery,Gallery_admin)
admin.site.register(Activitie,Activitie_admin)
admin.site.register(Program,Program_admin)
admin.site.register(ContactForm,ContactForm_admin)
admin.site.register(Home_Image,Home_Image_admin)