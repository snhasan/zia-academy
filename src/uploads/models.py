from django.db import models
from datetime import datetime
	

class upload(models.Model):
	Subject_Choice = (
			('Business', 'Business'),
			('Economics', 'Economics'),
			('Commerce','Commerce'),
			('Bangladesh_studies' ,'Bangladesh Studies'),
			('Accounting','Accounting'),
			('Banking_Finance','Banking and Finance'),
			('Business_Entrepreneurship','Business Entrepreneurship'),
			('Geography', 'Geography'),
			('Statistics', 'Statistics'),
			('Language', 'Language'),
			('Exam', 'Exam')

		)

	Curriculum_Choice = (
			('NC_BISE', 'NC (BISE)'),
			('CIE', 'CIE'),
			('Edexcel','Edexcel'),
			('IB' ,'IB')
			

		)

	title 		= models.CharField(max_length = 25)
	subject 	= models.CharField(max_length = 25, choices = Subject_Choice)
	curriculum  = models.CharField(max_length = 25, choices = Curriculum_Choice)
	description = models.TextField(blank = True, null=True)
	file        = models.FileField(upload_to='static/')
	date        = models.DateTimeField(default=datetime.now, blank=True)
	
	def __str__(self):
	   return self.title