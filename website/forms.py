from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from .models import PostModel


class PostForm(forms.ModelForm):
    class Meta:
        model = PostModel
        fields = ["username", "text", "img"]

class CustomUserCreationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["email"].widget.attrs.update({
            "type":"email",
            "id":"email",
            "name":"email",
            "placeholder":"Enter Your School Email",
            "required": "",
        })
        self.fields["username"].widget.attrs.update({
            "type":"text",
            "id":"username",
            "name":"username",
            "placeholder":"Enter Username",
            "required": ""
        })
        self.fields["password1"].widget.attrs.update({
            "type":"password",
            "id":"password1",
            "name":"password1",
            "placeholder":"Enter Password",
            "required": ""
        })
        self.fields["password2"].widget.attrs.update({
            "type":"password",
            "id":"password2",
            "name":"password2",
            "placeholder":"Confirm Password",
            "required": ""
        })
        self.fields["grade"].widget.attrs.update({
            "type":"number",
            "id":"email",
            "name":"email",
            "placeholder":"Enter Grade Level",
            "required": "",
            "min":"1",
            "max":"12"
        })

    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput,
        required=True
    )
    password2 = forms.CharField(
        label="Confirm Password",
        widget=forms.PasswordInput,
        required=True
    )
    email = forms.EmailField(
        label="Email Address",
        required=True,
        help_text="Must end with @students.uplifteducation.org"
    )
    username = forms.CharField(
        label="Username",
        max_length=50,
        required=True,
        validators=[]
    )
    grade = forms.IntegerField(
        label="Grade",
        min_value=1,
        max_value=12,
        required=True
    )

    class Meta:
        model = User
        fields = ["email", "username", "password1", "password2", "grade"]
    
    def clean_email(self):
        email = self.cleaned_data.get("email")
        if not email.endswith("@students.uplifteducation.org"):
            raise forms.ValidationError("Email must end with @students.uplifteducation.org")
        if User.objects.filter(email=self.cleaned_data["email"]).exists():
            raise forms.ValidationError("Email is already registered")
        return email

    def clean_password1(self):
        password1 = self.cleaned_data.get("password1")
        if not password1:
            raise forms.ValidationError("This field cannot be empty")
        return password1
    
    def check_password(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 != password2:
            raise forms.ValidationError("Password doesn't match")
        return password2, password1
    
    def clean_username(self):
        username = self.cleaned_data.get("username")
        if not username:
            raise forms.ValidationError("This field cannot be empty")
        return username


