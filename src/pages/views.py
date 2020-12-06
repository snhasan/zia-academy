from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from django.db import models
from django.http import HttpResponseRedirect

from .forms import ContactFormSave


from myBlogs.models import myBlog
from uploads.models import upload
from pages.models import About,Team,faq,services,Profile,Activitie,Program,ContactForm
from django.core.mail import send_mail


# Create your views here.
def home_view(request, *args, **kwargs):
	Activities = Activitie.objects.order_by("-date")[:3]

	service = services.objects.all()
	servs = services.objects.order_by("-date")[:6]

	about = About.objects.latest("date")
	profile = Profile.objects.latest("date")
	teams = Team.objects.order_by("-date")[:4]

	faqs = faq.objects.order_by("-date")[:4]

	context = {
	'Activities' : Activities,
	'service' : service,
	'about' : about,
	'teams':teams,
	'servs': servs,
	'profile' : profile,
	'faqs' : faqs
	}

	return render(request, "index.html", context)

def about_view(request, *args, **kwargs):

	service = services.objects.all()

	about = About.objects.latest("date")
	teams = Team.objects.all()
	profile = Profile.objects.latest("date")

	context = {
	
	'service' : service,
	'about' : about,
	'teams' : teams,
	'profile' : profile
	}

	return render(request, "about.html", context)

def programs_view(request, *args, **kwargs):

	programs = Program.objects.all()

	profile = Profile.objects.latest("date")


	context = {
	'programs' : programs,
	'profile' : profile,
	}

	return render(request, "programs.html", context)
	

def programs_details_view(request, pk=None):


	obj = Program.objects.get(pk=pk)
	programs = Program.objects.order_by("-date")[:4]
	profile = Profile.objects.latest("date")

	context = {
	'programs' : programs,
	'obj' : obj,
	'profile' : profile,
	}

	return render(request, "program_details.html", context)

def gallery_view(request, *args, **kwargs):

	service = services.objects.all()

	about = About.objects.latest("date")
	teams = Team.objects.all()
	profile = Profile.objects.latest("date")

	context = {
	
	'service' : service,
	'about' : about,
	'teams' : teams,
	'profile' : profile
	}

	return render(request, "gallery.html", context)


def activities_view(request,  *args, **kwargs):

	Activities = Activitie.objects.all()
	profile = Profile.objects.latest("date")


	context = {
	'Activities' : Activities,
	'profile' : profile,
	}

	return render(request, "activities.html", context)


def activities_details_view(request, pk=None):


	obj = Activitie.objects.get(pk=pk)
	Activities = Activitie.objects.order_by("-date")[:4]
	profile = Profile.objects.latest("date")

	context = {
	'Activities' : Activities,
	'profile' : profile,
	'obj' : obj,
	}

	return render(request, "activities-details.html", context)

def contact_view(request, *args, **kwargs):

	service = services.objects.all()
	profile = Profile.objects.latest("date")

	context = {
	'service' : service,
	'profile' : profile
	}

	return render(request, "contact.html", context)

def contact_form_view(request, pk=None):

	form = ContactFormSave(request.POST or None)
	if form.is_valid():
		form.save()


	profile = Profile.objects.latest("date")
	
	context = {
	'profile' : profile
	}

	return render(request, "contact.html", context)


def blog_view(request, *args, **kwargs):
	return render(request, "blog.html", {})

def blog_details_views(request, *args, **kwargs):
	return render(request, "blog-detail.html", {})

def sendMail(request):

	service = services.objects.all()
	profile = Profile.objects.latest("date")

	context = {

	'service' : service,
	'profile' : profile
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