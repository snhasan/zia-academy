from django.db import models
from datetime import datetime

class blogComment(models.Model):

	blog_id		= models.IntegerField()
	comentor_name 		= models.CharField(max_length = 25,blank = True, null=True)
	email 		= models.CharField(max_length = 50,blank = True, null=True)
	message		= models.TextField(blank = True, null=True)
	date        = models.DateTimeField(default=datetime.now, blank=True)

	def __str__(self):
	   return self.comentor_name