from django.shortcuts import render
from django.db import models

from .forms import CommentForm

from .models import blogComment
from myBlogs.models import myBlog


def comment_create_view(request, pk=None):

	form = CommentForm(request.POST or None)
	if form.is_valid():
		form.save()

	blog_id = form.cleaned_data['blog_id']
	
	obj = myBlog.objects.get(pk=blog_id)
	obj2 = blogComment.objects.filter(blog_id=blog_id)

	context = {
	'object' : obj,
	'object2' : obj2
	}
	
	return render(request, "blog-detail.html", context)

