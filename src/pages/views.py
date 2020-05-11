from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings

from myBlogs.models import myBlog
from uploads.models import upload
from django.core.mail import send_mail


# Create your views here.
def home_view(request, *args, **kwargs):
	obj = myBlog.objects.order_by("-date")[:3]

	ncs = upload.objects.filter(
	    curriculum='NC_BISE'
	).values('subject').distinct()

	cies = upload.objects.filter(
	    curriculum='CIE'
	).values('subject').distinct()

	edexcels = upload.objects.filter(
	    curriculum='Edexcel'
	).values('subject').distinct()

	ibs = upload.objects.filter(
	    curriculum='IB'
	).values('subject').distinct()

	context = {
	'object' : obj,
	'ncs' : ncs,
	'cies' : cies,
	'edexcels' : edexcels,
	'ibs' : ibs
	}

	return render(request, "index.html", context)

def about_view(request, *args, **kwargs):

	ncs = upload.objects.filter(
	    curriculum='NC_BISE'
	).values('subject').distinct()

	cies = upload.objects.filter(
	    curriculum='CIE'
	).values('subject').distinct()

	edexcels = upload.objects.filter(
	    curriculum='Edexcel'
	).values('subject').distinct()

	ibs = upload.objects.filter(
	    curriculum='IB'
	).values('subject').distinct()

	context = {
	'ncs' : ncs,
	'cies' : cies,
	'edexcels' : edexcels,
	'ibs' : ibs
	}

	return render(request, "about.html", context)

def subject_view(request, curriculum, subject):

	ncs = upload.objects.filter(
	    curriculum='NC_BISE'
	).values('subject').distinct()

	cies = upload.objects.filter(
	    curriculum='CIE'
	).values('subject').distinct()

	edexcels = upload.objects.filter(
	    curriculum='Edexcel'
	).values('subject').distinct()

	ibs = upload.objects.filter(
	    curriculum='IB'
	).values('subject').distinct()

	topics = upload.objects.filter(
		curriculum=curriculum, subject=subject) 

	context = {
	'ncs' : ncs,
	'cies' : cies,
	'edexcels' : edexcels,
	'ibs' : ibs,
	'topics' : topics
	}

	return render(request, "subject-details.html", context)

def contact_view(request, *args, **kwargs):

	ncs = upload.objects.filter(
	    curriculum='NC_BISE'
	).values('subject').distinct()

	cies = upload.objects.filter(
	    curriculum='CIE'
	).values('subject').distinct()

	edexcels = upload.objects.filter(
	    curriculum='Edexcel'
	).values('subject').distinct()

	ibs = upload.objects.filter(
	    curriculum='IB'
	).values('subject').distinct()

	context = {
	'ncs' : ncs,
	'cies' : cies,
	'edexcels' : edexcels,
	'ibs' : ibs
	}

	return render(request, "contact.html", context)


def blog_view(request, *args, **kwargs):
	return render(request, "blog.html", {})

def blog_details_views(request, *args, **kwargs):
	return render(request, "blog-detail.html", {})

def sendMail(request):

	ncs = upload.objects.filter(
	    curriculum='NC_BISE'
	).values('subject').distinct()

	cies = upload.objects.filter(
	    curriculum='CIE'
	).values('subject').distinct()

	edexcels = upload.objects.filter(
	    curriculum='Edexcel'
	).values('subject').distinct()

	ibs = upload.objects.filter(
	    curriculum='IB'
	).values('subject').distinct()

	context = {
	'ncs' : ncs,
	'cies' : cies,
	'edexcels' : edexcels,
	'ibs' : ibs
	}


	data = request.POST
	from_email = settings.EMAIL_HOST_USER
	s_name = request.POST['name']
	s_email = request.POST['email']
	message = request.POST['message']
	subject = request.POST['subject']

	name = s_name + "   " + s_email
	


	send_mail(name,
		message,
		from_email,
		['snhasan05@gmail.com'],
		fail_silently= False)

	return render(request, "contact.html", context)