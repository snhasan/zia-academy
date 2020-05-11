from django import forms

from blogComment.models import blogComment

class CommentForm(forms.ModelForm):
	class Meta:
		model = blogComment
		fields = [
			'comentor_name',
			'email',
			'message',
			'blog_id'
		]