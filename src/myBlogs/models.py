from django.db import models
from datetime import datetime
	

class myBlog(models.Model):

	title 		= models.CharField(max_length = 120)
	description = models.TextField(blank = True, null=True)
	images        = models.ImageField(null = True, blank = True)
	date        = models.DateTimeField(default=datetime.now, blank=True)

	def __str__(self):
	   return self.title