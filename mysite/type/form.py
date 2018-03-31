from django import forms
from django.utils.translation import gettext_lazy as _
from .models import Info, Summary, Applying, ApplyingAs

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
class ApplyForm(forms.ModelForm):
	class Meta:
		model = Applying
		fields = ('author', 'charLib','timeLib',)

class NameForm(forms.ModelForm):
	class Meta:
		model = Summary
		fields = ('author','comboListText','medListText','newID')

class ChoiceForm(forms.ModelForm):
	class Meta:
		model = ApplyingAs
		fields = ('choice',)
	def __init__(self, *args, **kwargs):
		super(ChoiceForm, self).__init__(*args, **kwargs)
		NAMES = []
		for n in Summary.objects.all():
			NAMES.append((str(n),(n)))
		self.fields['choice'] = forms.ChoiceField(choices = NAMES)