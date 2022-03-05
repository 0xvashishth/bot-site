from django import forms
from .models import user


class UsersForm(forms.ModelForm):

	class Meta:

		model = user

		fields=[
			"first_name",
			"last_name",
			"email",
			"phone",
			"username",
			"password",
            "Address",
			"reason",
		]