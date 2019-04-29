from django.contrib import admin
from .models import Author
# Register your models here.
from dashboard.models import myuser
from django.contrib.auth.admin import UserAdmin
from django.contrib import admin
from django.apps import AppConfig


class DashboardConfig(AppConfig):
    name = 'dashboard'




class testss(admin.ModelAdmin):
    pass


class test(UserAdmin):
    pass




# Register your models here.
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    fields = (('email', 'title'),"address","tel")
    list_display = ('email', 'title')
    list_filter=("email",)


admin.site.register(myuser)
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserCreateForm(UserCreationForm):
    email = forms.EmailField(required = True)
    job = forms.CharField(required=True,max_length=50)
    age = forms.IntegerField()

    class Meta:
        model = User
        fields = ("username", "email","job", "password1", "password2")

    def save(self, commit=True):
        user = super(UserCreateForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user