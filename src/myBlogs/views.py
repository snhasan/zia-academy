from django.shortcuts import render

from .models import myBlog

from blogComment.models import blogComment
from uploads.models import upload


def blog_view(request):
	obj = myBlog.objects.all().order_by("-date")

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

	return render(request, "blog.html", context)

def blog_details_view(request, pk=None):
	
	obj = myBlog.objects.get(pk=pk)
	obj2 = blogComment.objects.filter(blog_id=pk)

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
	'object2' : obj2,
	'ncs' : ncs,
	'cies' : cies,
	'edexcels' : edexcels,
	'ibs' : ibs
	}
	
	return render(request, "blog-detail.html", context)


