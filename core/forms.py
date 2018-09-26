from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=50, required=False, help_text='Optional')
    first_name.widget.attrs.update({'placeholder': "Enter your first name",
                                    'id': "first_name",
                                    'class': "validate"
                                    })
    last_name = forms.CharField(max_length=50, required=False, help_text='Optional')
    last_name.widget.attrs.update({'placeholder': "Enter your last name",
                                   'id': "last_name",
                                   'class': "validate"})

    email = forms.EmailField(max_length=50, required=True, help_text='Required field. Inform a valid email address')
    email.widget.attrs.update({"id": "email",
                               "class": "validate",
                               "placeholder": "Enter your email"})

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({
            'autocomplete': 'off',
            'placeholder': "Placeholder",
            'id': "username",
            'class': "validate"

        })
        self.fields['password1'].widget.attrs.update({
            'id': 'password',
            'class': 'validate'
        })
        self.fields['password2'].widget.attrs.update({
                'id': 'password',
                'class': 'validate'
        })

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')
