from django.db import models
from datetime import datetime
	

class About(models.Model):

	title 			 = models.CharField(max_length = 120)
	goals    		 = models.TextField(blank = True, null=True)
	goals_summary    = models.TextField(blank = True, null=True)
	goals_description= models.TextField(blank = True, null=True)
	mission     	 = models.TextField(blank = True, null=True)
	mission_summary  = models.TextField(blank = True, null=True)
	mission_description = models.TextField(blank = True, null=True)
	objective     	= models.TextField(blank = True, null=True)
	objective_summary  = models.TextField(blank = True, null=True)
	objective_description = models.TextField(blank = True, null=True)
	date        	= models.DateTimeField(default=datetime.now, blank=True)

	def __str__(self):
	   return self.title

class Team(models.Model):

	name 		= models.CharField(max_length = 120)
	designation = models.CharField(max_length = 120)
	email       = models.EmailField(blank = True, null=True)
	phone       = models.CharField(max_length = 120,blank = True, null=True)
	linkedIn    = models.CharField(max_length = 120,blank = True, null=True)
	facebook    = models.CharField(max_length = 120,blank = True, null=True)
	image       = models.ImageField(null = True, blank = True)
	description = models.TextField(blank = True, null=True)
	date        = models.DateTimeField(default=datetime.now, blank=True)

	def __str__(self):
	   return self.name	   

class Activitie(models.Model):

	title 		= models.CharField(max_length = 120)
	summary     = models.TextField(blank = True, null=True)
	description = models.TextField(blank = True, null=True)
	image       = models.ImageField(null = True, blank = True)
	date        = models.DateTimeField(default=datetime.now, blank=True)

	def __str__(self):
	   return self.title		   

class Program(models.Model):

	title 		= models.CharField(max_length = 120)
	summary     = models.TextField(blank = True, null=True)
	description = models.TextField(blank = True, null=True)
	image       = models.ImageField(null = True, blank = True)
	date        = models.DateTimeField(default=datetime.now, blank=True)

	def __str__(self):
	   return self.title	   

class faq(models.Model):

	question    = models.TextField(blank = True, null=True)
	answer      = models.TextField(blank = True, null=True)
	date        = models.DateTimeField(default=datetime.now, blank=True)

	def __str__(self):
	   return self.question

class services(models.Model):

	title 		= models.CharField(max_length = 120)
	summary     = models.TextField(blank = True, null=True)
	description = models.TextField(blank = True, null=True)
	image       = models.ImageField(null = True, blank = True)
	date        = models.DateTimeField(default=datetime.now, blank=True)

	def __str__(self):
	   return self.title

class Profile(models.Model):

	name 		= models.CharField(max_length = 120)
	address     = models.CharField(max_length = 120,blank = True, null=True)
	email_1       = models.EmailField(blank = True, null=True)
	email_2       = models.EmailField(blank = True, null=True)
	phone_1      = models.CharField(max_length = 120,blank = True, null=True)
	phone_2      = models.CharField(max_length = 120,blank = True, null=True)
	image       = models.ImageField(null = True, blank = True)
	date        = models.DateTimeField(default=datetime.now, blank=True)

	def __str__(self):
	   return self.name


class Gallery(models.Model):

	title 		= models.CharField(max_length = 120)
	image       = models.ImageField(null = True, blank = True)
	date        = models.DateTimeField(default=datetime.now, blank=True)

	def __str__(self):
	   return self.title


class Home_Image(models.Model):

	title 		= models.CharField(max_length = 120)
	image1       = models.ImageField(null = True, blank = True)
	image2       = models.ImageField(null = True, blank = True)
	image3       = models.ImageField(null = True, blank = True)
	image3       = models.ImageField(null = True, blank = True)
	date        = models.DateTimeField(default=datetime.now, blank=True)

	def __str__(self):
	   return self.title


class ContactForm(models.Model):

	name 		= models.CharField(max_length = 120)
	email 		= models.EmailField(blank = True, null=True)
	message     = models.TextField(blank = True, null=True)
	date        = models.DateTimeField(default=datetime.now, blank=True)

	def __str__(self):
	   return self.name