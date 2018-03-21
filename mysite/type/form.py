from django import forms
from django.utils.translation import gettext_lazy as _
from .models import Info

class PostForm(forms.ModelForm):
	class Meta:
		model = Info
		fields = ('author', 'charLib','timeLib',)
		widgets = {
			'author': forms.Textarea(attrs={'cols': 100, 'rows': 1})
		}
		help_texts = {
			'author': _('\nSome useful help text.'),
		}
		error_messages = {
			'author': {
				'max_length': _("This writer's name is too long."),
			},
		}
class NameForm(forms.Form):
	model = Info
	Info.author = forms.CharField(max_length = 200)
	Info.charLib = forms.CharField(max_length = 20000)
	Info.timeLib = forms.CharField(max_length = 20000)
	def save(commit):
		Input.publish(commit)