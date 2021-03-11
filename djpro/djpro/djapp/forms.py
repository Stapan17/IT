from django import forms
from .models import userInfo, Category, jobPost
from django.contrib.auth.models import User


choices = Category.objects.all().values_list('name', 'name')

choice_list = []

for item in choices:
    choice_list.append(item)


class userForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ['email', 'username', 'password']


class userInfoForm(forms.ModelForm):
    class Meta():
        model = userInfo
        fields = ['name', 'phone', 'profile_pic']


class userInfoUpdateForm(forms.ModelForm):
    class Meta():
        model = userInfo
        fields = ("name", "phone", "profile_pic")

    def save(self, commit=True):
        user_info = self.instance
        user_info.name = self.cleaned_data['name']
        user_info.phone = self.cleaned_data['phone']

        if self.cleaned_data['profile_pic']:
            user_info.profile_pic = self.cleaned_data['profile_pic']

        if commit:
            user_info.save()

        return user_info


class jobPostForm(forms.ModelForm):
    class Meta():
        model = jobPost
        fields = ("company", "position", "location",
                  "salaryL", "salaryH", "min_exp", "description", "resume", "category", "person")

        widgets = {
            "person": forms.TextInput(attrs={'class': 'form-control', 'value': '', 'id': 'elder', 'type': 'hidden'}),
            "category": forms.Select(choices=choice_list, attrs={'class': 'form-control'})
        }
