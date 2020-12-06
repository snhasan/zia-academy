from django import forms

from pages.models import ContactForm

class ContactFormSave(forms.ModelForm):
	class Meta:
		model = ContactForm
		fields = [
			'name',
			'email',
			'message'
		]