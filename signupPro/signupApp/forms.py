# Create a ModelForm in forms.py. Django makes accepting form input and passing it to a model.
# Instead of inheriting from the forms.Forms class, use forms.ModelForm in our forms.py file.
# This helper class allows us to create a form (NewUserForm) from a pre-existing model (here User model).
# Then add an inline class called Meta. This Meta class provides information connecting the model to
# the form. (i.e., Meta class to map model fields with form fields).

from django import forms
from .models import User


class NewUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'
